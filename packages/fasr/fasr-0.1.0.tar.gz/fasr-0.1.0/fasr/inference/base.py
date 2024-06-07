import requests
from io import BytesIO
import librosa
from ..utils import timer
import numpy as np
from typing import Dict, ByteString
import traceback
from loguru import logger
import re


class ASRInference:
    """ASR wpai 服务推理基类，一般情况下只需要实现inference和setup方法"""

    @timer("load audio")
    def load_audio(self, content, sr: int = 16000) -> np.array:
        file = BytesIO(content)
        audio, sr = librosa.load(file, mono=False, sr=sr)
        return audio

    @timer("predict")
    def predict(self, url: str, **kwargs) -> Dict[str, str]:
        res = {}
        try:
            response = requests.get(url=url)
            if response.status_code == 200:
                audio = self.load_audio(response.content)
                channals = len(audio.shape)
                if channals != 2:
                    res["data"] = ""
                    res["code"] = 0
                    res["msg"] = "输入的音频是单声道，不解析"
                else:
                    ds = len(audio[0]) / 16000
                    logger.info(f"audio duration seconds {ds}")
                    if ds < 0.5:
                        res["data"] = ""
                        res["code"] = 0
                        res["msg"] = f"输入的音频太短了{ds}s，不解析"
                    elif (
                        ds >= self.max_duration_saconds
                    ):  # 超过2个小时的超长音频，这里不做解析。
                        res["data"] = ""
                        res["code"] = 0
                        res["msg"] = "音频时长超过2小时，不解析"
                    else:
                        d_left, d_right = self.inference([audio[0], audio[1]])

                        data = self.post_process(d_left, d_right)

                        res["data"] = data
                        res["code"] = 0
                        res["msg"] = "success"
            else:
                res["code"] = -1
                res["msg"] = "download failure" + str(response)
                res["data"] = ""

        except Exception as e:
            errorMsg = "traceback.format_exc():\n%s" % traceback.format_exc()
            logger.error(errorMsg)
            logger.error(e.args)
            logger.error("url:{}".format(url))
            res["code"] = -1
            res["data"] = ""
            res["msg"] = "程序异常请联系管理员！" + errorMsg

        return res

    @timer("post process")
    def post_process(self, d_left, d_right):
        data = dict()
        sentence_all = []
        text_all = dict()
        text_all["left"] = ""
        text_all["right"] = ""

        if "text" in d_left:
            text_all["left"] = d_left["text"].replace(" ", "")
        if "sentence_info" in d_left:
            for s in d_left["sentence_info"]:
                s["text"] = re.sub(r"[^\w\s]", "", s["text"])
                s["startTime"] = s["timestamp"][0][0]
                s["endTime"] = s["timestamp"][-1][1]
                s["duration"] = s["endTime"] - s["startTime"]
                s["channel"] = "left"
                del s["start"]
                del s["end"]
                del s["timestamp"]
            sentence_all += d_left["sentence_info"]

        if "text" in d_right:
            text_all["right"] = d_right["text"].replace(" ", "")
        if "sentence_info" in d_right:
            for s in d_right["sentence_info"]:
                s["text"] = re.sub(r"[^\w\s]", "", s["text"])
                s["startTime"] = s["timestamp"][0][0]
                s["endTime"] = s["timestamp"][-1][1]
                s["duration"] = s["endTime"] - s["startTime"]
                s["channel"] = "right"
                del s["start"]
                del s["end"]
                del s["timestamp"]
            sentence_all += d_right["sentence_info"]

        sentence_all.sort(key=lambda x: x["startTime"])
        for idx, _ in enumerate(sentence_all):
            sentence_all[idx]["sentenceIndex"] = idx

        data["text"] = text_all
        data["sentences"] = sentence_all
        return data

    def inference(self):
        raise NotImplementedError()

    def setup(self):
        raise NotImplementedError()

    def eval(self, *args, **kwargs):
        pass

    def to(self, *args, **kwargs):
        pass
