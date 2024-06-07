from ..utils import timer
from typing import Tuple, Dict, List
from .base import ASRInference
import numpy as np
from lightning_utilities.core.imports import package_available


def pad_feats(feats: List[np.ndarray], max_feat_len: int) -> np.ndarray:
    def pad_feat(feat: np.ndarray, cur_len: int) -> np.ndarray:
        pad_width = ((0, max_feat_len - cur_len), (0, 0))
        return np.pad(feat, pad_width, "constant", constant_values=0)

    feat_res = [pad_feat(feat, feat.shape[0]) for feat in feats]
    feats = np.array(feat_res).astype(np.float32)
    return feats


def load_data(wav_contents: List[np.ndarray], fs: int):
    return wav_contents


class OnnxInference(ASRInference):
    def __init__(
        self,
        model_dir: str = "checkpoints/iic/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch",
        punc_dir: str = "checkpoints/iic/punc_ct-transformer_zh-cn-common-vocab272727-pytorch",
        batch_size: int = 20,
        max_duration_saconds: int = 7200,
        quantize: bool = False,
        use_cpu: bool = False,
        num_threads: int = 4,
    ):
        super().__init__()

        self.model_dir = model_dir
        self.punc_dir = punc_dir
        self.batch_size = batch_size
        self.max_duration_saconds = max_duration_saconds
        self.quantize = quantize
        self.device_id = -1 if use_cpu else 0
        self.num_threads = num_threads

        _ = self.setup()

    @timer("load model")
    def setup(self):
        funasr_onnx_installed = package_available('funasr_onn')
        if funasr_onnx_installed:
            from funasr_onnx import Paraformer, CT_Transformer
            
        self.model = Paraformer(
            self.model_dir,
            quantize=self.quantize,
            device_id=self.device_id,
            intra_op_num_threads=self.num_threads,
            batch_size=self.batch_size,
        )
        self.model.load_data = load_data
        self.punc_model = CT_Transformer(
            self.punc_dir,
            quantize=self.quantize,
            device_id=self.device_id,
            intra_op_num_threads=self.num_threads,
        )

    @timer("extract feats")
    def extract_feat(
        self, waveform_list: List[np.ndarray]
    ) -> Tuple[np.ndarray, np.ndarray]:
        feats, feats_len = [], []
        for waveform in waveform_list:
            speech, _ = self.frontend.fbank(waveform)
            feat, feat_len = self.frontend.lfr_cmvn(speech)
            feats.append(feat)
            feats_len.append(feat_len)

        feats = pad_feats(feats, np.max(feats_len))
        feats_len = np.array(feats_len).astype(np.int32)
        return feats, feats_len

    @timer("inference")
    def inference(self, audios: List[np.ndarray]):
        asr_results = self.model(audios)
        for asr_result in asr_results:
            punc_result = self.punc_model(asr_result["preds"])
            _ = self.append_sentence_info(asr_result, punc_result)
        return asr_results

    def append_sentence_info(self, asr_result, punc_result):
        punc_ids = []
        for idx, r in enumerate(punc_result[1]):
            if r != 1:
                punc_ids.append(idx)
        asr_text = punc_result[0]
        sentence_infos = []
        for i, id in enumerate(punc_ids):
            sentence_info = {"text": "", "start": "", "end": "", "timestamp": []}
            if i == 0:
                text = asr_text[: id + 2]
            else:
                pre = punc_ids[i - 1]
                text = asr_text[pre + 1 + i : id + 2 + i]
            sentence_info["text"] = text
            timestamp = asr_result["timestamp"][: id + 1]
            sentence_info["timestamp"] = timestamp
            sentence_info["start"] = timestamp[0][0]
            sentence_info["end"] = timestamp[-1][-1]
            sentence_infos.append(sentence_info)
        asr_result["sentence_info"] = sentence_infos
        asr_result["text"] = asr_text
        if "raw_tokens" in asr_result:
            del asr_result["raw_tokens"]
        return asr_result
