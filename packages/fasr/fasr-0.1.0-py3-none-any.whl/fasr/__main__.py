from jsonargparse import CLI
from .inference import TorchInference, OnnxInference


class Test:
    """测试pytorch和onnx runtime推理速度"""

    def __init__(
        self,
        model_dir: str = "checkpoints/iic/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch",
        punc_dir: str = "checkpoints/iic/punc_ct-transformer_zh-cn-common-vocab272727-pytorch",
        vad_dir: str = "checkpoints/iic/speech_fsmn_vad_zh-cn-16k-common-pytorch",
        n: int = 10,
    ):
        super().__init__()

        self.model_dir = model_dir
        self.punc_dir = punc_dir
        self.vad_dir = vad_dir
        self.n = n

    def pytorch(self, url: str):
        """测试pytorch推理速度

        Args:
            url (str): 音频数据地址
        """
        infer = TorchInference(
            model_dir=self.model_dir, punc_dir=self.punc_dir, vad_dir=self.vad_dir
        )
        for i in range(self.n):
            result = infer.predict(url)

    def onnx(
        self,
        url: str,
        quantize: bool = False,
        use_cpu: bool = False,
        num_threads: int = 4,
    ):
        """测试onnx runtime推理速度

        Args:
            url (str): 音频地址
            quantize (bool, optional): 是否使用量化模型. Defaults to False.
            use_cpu (bool, optional): 是否使用cpu. Defaults to False.
            num_threads (int, optional): 使用cpu推理的物理核数量. Defaults to 4.
        """
        infer = OnnxInference(
            model_dir=self.model_dir,
            punc_dir=self.punc_dir,
            quantize=quantize,
            use_cpu=use_cpu,
            num_threads=num_threads,
        )
        for i in range(self.n):
            result = infer.predict(url)


def prepare_models():
    from modelscope import snapshot_download

    models = [
        "iic/punc_ct-transformer_zh-cn-common-vocab272727-pytorch",
        "iic/speech_fsmn_vad_zh-cn-16k-common-pytorch",
        "iic/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch",
        "iic/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch",
    ]
    for model in models:
        snapshot_download(model_id=model, cache_dir="checkpoints")

def download(model: str, revision: str = None, cache_dir: str = 'chechkpoints'):
    from modelscope import snapshot_download
    model = snapshot_download(model, cache_dir=cache_dir, revision=revision)


commands = {"test": Test, "prepare": prepare_models, "download": download}


def run():
    CLI(commands)


if __name__ == "__main__":
    run()
