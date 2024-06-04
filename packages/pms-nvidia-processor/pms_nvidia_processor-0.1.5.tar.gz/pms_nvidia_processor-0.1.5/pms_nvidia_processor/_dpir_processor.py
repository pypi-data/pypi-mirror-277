import subprocess
from ._dependency import *
from ._const import *
from . import patcher


def _pre_processing(
    batch_input_images: List[np.ndarray],
    input_buffer: np.ndarray,
) -> None:
    b = len(batch_input_images)
    for batch_idx in range(b):
        image = batch_input_images[batch_idx]
        h, w, c = image.shape
        for channel_idx in range(c):
            np.divide(
                image[:, :, channel_idx],
                255,
                out=input_buffer[batch_idx, channel_idx, :h, :w],
            )


def _post_processing(
    output_buffer: np.ndarray,  # BxCxHxW
    output_image: np.ndarray,  # BxHxWxC
) -> None:
    b, h, w, c = output_image.shape
    denoise_pred = np.clip(
        np.multiply(output_buffer[:b, :, :h, :w], 255), 0, 255
    ).astype(np.uint8)
    for i in range(3):
        np.copyto(src=denoise_pred[:, i, :, :], dst=output_image[:, :, :, i])


@register
class DPIRProcessor(IEngineProcessor[EngineIOData, EngineIOData]):
    def __init__(
        self,
        concurrency: int,
        index: int,
        model_path: str,
        device_name: str = "cuda",
    ):
        for k, v in os.environ.items():
            logger.critical(f"DPIRProcessor[{index}]>>NodeEnv {k}:{v} ")
        # set member var
        self.index = index
        self.model_path = model_path
        self.device_name = device_name
        self._concurrency = concurrency

        # set loop policy
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

        # set device_id
        device_count = TRT.get_device_count()
        device_id = index % device_count
        self.device_id = device_id
        os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
        os.environ["CUDA_VISIBLE_DEVICES"] = "all"
        # start init
        logger.info(f"{self.__class__}[{index}]>> Init Start")

        # super
        super().__init__(
            concurrency=concurrency,
            index=index,
        )

        # end init
        logger.info(f"{self.__class__}[{index}]>> Init END")

    async def inference(self, batch_input_data: List[np.ndarray]) -> List[np.ndarray]:
        session = self.session
        patch_size = DPIRConfig.PATCH_SIZE
        batch = len(batch_input_data)
        batch_output_data: np.ndarray = np.zeros(
            (batch, patch_size, patch_size, 3), np.uint8
        )
        TACT = {}
        TACT["_pre_processing"] = time.time()
        _pre_processing(
            batch_input_images=batch_input_data,
            input_buffer=self.input_buffer,
        )
        session.run()
        _post_processing(
            output_buffer=self.output_buffer,
            output_image=batch_output_data,
        )
        # for key, value in TACT.items():
        #     logger.debug(f"TACT[{key}] : {-value*1000:.3f} ms")
        return [output_data for output_data in batch_output_data]  # unpack

    async def _run(self, input_data: EngineIOData) -> EngineIOData:
        max_batch_size = self.io_shapes["input"][0][0]
        # 여기서 patching
        input_image: np.ndarray = input_data.frame  # type: ignore
        padded_input_image = patcher.pad_vector(
            input_image, overlap_length=DPIRConfig.INPUT_OVERLAB_LENGTH
        )
        output_image: np.ndarray = np.zeros_like(input_image)

        # slice
        input_patches = self.patcher.slice(input_vector=padded_input_image)

        # batch inference
        output_patches = []
        for batch_items in TRT.batch(input_patches, max_batch_size):
            ops = await self.inference(batch_input_data=batch_items)
            output_patches += ops

        self.patcher.merge(output_vector=output_image, patches=output_patches)
        return EngineIOData(frame_id=input_data.frame_id, frame=output_image)

    def _ready_processor(self) -> bool:
        return True

    def _bind_io(self, input_data: EngineIOData):
        model_path = self.model_path
        device_id = self.device_id
        # set patcher

        input_image: np.ndarray = input_data.frame  # type: ignore
        padded_input_image = patcher.pad_vector(
            input_image, overlap_length=DPIRConfig.INPUT_OVERLAB_LENGTH
        )
        output_image: np.ndarray = np.zeros_like(input_image)
        self.input_vector_shape = padded_input_image.shape
        self.output_vector_shape = output_image.shape
        self.patcher = patcher.Patcher(
            input_vector_shape=self.input_vector_shape,  # type: ignore
            input_patch_shape=DPIRConfig.PATCHER_INPUT_PATCH_SHAPE,
            input_overlap_length=DPIRConfig.INPUT_OVERLAB_LENGTH,
            output_vector_shape=self.output_vector_shape,  # type: ignore
            output_patch_shape=DPIRConfig.PATCHER_OUTPUT_PATCH_SHAPE,
            output_overlap_length=DPIRConfig.OUTPUT_OVERLAB_LENGTH,
        )
        n_patches = len(self.patcher.slice(input_vector=padded_input_image))

        # set io shape
        self.batch_size = min(n_patches, DPIRConfig.MAX_BATCH_SIZE)
        self.io_shapes = {
            "input": (
                [DPIRConfig.MAX_BATCH_SIZE, *DPIRConfig.TRT_INPUT_PATCH_SHAPE],
                np.float32,
            ),
            "output": (
                [DPIRConfig.MAX_BATCH_SIZE, *DPIRConfig.TRT_OUTPUT_PATCH_SHAPE],
                np.float32,
            ),
        }

        # init trt engine
        logger.info(
            f"DPIRProcessor[{self.index}]>> Try Create session \n - path={model_path}\n - device_id={device_id}\n - io_shapes={self.io_shapes}"
        )
        proc = subprocess.Popen(["nvidia-smi"], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        logger.info(f"DPIRProcessor[{self.index}]>> smi status\n{out}")
        self.session = TRT.TRTSession(
            model_path=model_path,
            device_id=device_id,
            io_shapes=self.io_shapes,
        )

        # warm up
        self.session.run()

        # set io buffer
        self.input_buffer = self.session._input_bindings[0].host_buffer.reshape(
            self.io_shapes["input"][0]
        )
        self.input_buffer.fill(1.0 / 255.0)
        self.output_buffer = self.session._output_bindings[0].host_buffer.reshape(
            *self.io_shapes["output"][0]
        )

        return True

    def _get_live(self) -> bool:
        return True

    def _get_concurrency(self) -> int:
        return self._concurrency
