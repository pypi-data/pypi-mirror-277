from funasr import AutoModel
from ..utils import timer
from .base import ASRInference


class TorchInference(ASRInference):
    """基于funasr的自动语音识别"""

    def __init__(
        self,
        model_dir: str = "checkpoints/iic/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch",
        vad_dir: str = "checkpoints/iic/speech_fsmn_vad_zh-cn-16k-common-pytorch",
        punc_dir: str = "checkpoints/iic/punc_ct-transformer_zh-cn-common-vocab272727-pytorch",
        batch_size_s: int = 30,
        max_duration_saconds: int = 7200,
    ):
        super().__init__()

        self.model_dir = model_dir
        self.vad_dir = vad_dir
        self.punc_dir = punc_dir
        self.batch_size_s = batch_size_s
        self.max_duration_saconds = max_duration_saconds

        self.pipe = self.setup()

    @timer("load models")
    def setup(self) -> AutoModel:
        pipe = AutoModel(
            model=self.model_dir,
            vad_model=self.vad_dir,
            punc_model=self.punc_dir,
            sentence_timestamp=True,
            return_raw_text=False,
            batch_size_s=self.batch_size_s,
        )
        return pipe

    @timer("inference")
    def inference(self, audios):
        results = []
        for audio in audios:
            result = self.pipe.generate(input=audio)
            result = result[0] if len(result) > 0 else {}
            results.append(result)
        return results
