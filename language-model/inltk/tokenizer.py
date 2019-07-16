from fastai.text import *
import sentencepiece as spm

class SanskritTokenizer(BaseTokenizer):
    def __init__(self, lang:str):
        self.lang = lang
        self.sp = spm.SentencePieceProcessor()
        self.sp.Load(str("/home/gaurav/PycharmProjects/nlp-for-sanskrit/tokenizer/sanskrit_lm.model"))
        
    def tokenizer(self, t:str) -> List[str]:
        return self.sp.EncodeAsPieces(t)
