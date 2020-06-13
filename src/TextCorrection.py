
# -*- coding: utf-8 -*-
"""
@Software:spyder
@File:TextCorrection.py
@Created on Thu Jun  4 16:08:47 2020
@author: betty
@description:文本纠错，支持文本中拼音，英文，错词的转中文
"""
import re
from PinYinChar import PinYinChar 
from DealChar import _extract_character,_extract_num,_extract_letter,_chinese_to_english
from NumberToHanzi import NumberToHanzi 
import pycorrector
NumberToHanzi=NumberToHanzi()
PinYinChar=PinYinChar()

class TextCorrection():
    
    def __init__(self):
        self.text = ''
        
    # def _english_sentenc(self,sentenc):
    #     sentenc=sentenc.replace(_extract_letter(sentenc),_chinese_to_english(_extract_letter(sentenc)))
    #     if  len(_extract_num(sentenc)):
    #         return sentenc.replace(_extract_num(sentenc),NumberToHanzi.dig2cn(_extract_num(sentenc)))
    #     else:
    #         return sentenc
        
    
    def _pinyin_sentenc(self,sentenc):
        sentenc=_chinese_to_english(sentenc)
        sentenc=sentenc.replace(_extract_letter(sentenc),PinYinChar.pinyin_2_hanzi_output(_extract_letter(sentenc)))
        if  len(_extract_num(sentenc)):
            return sentenc.replace(_extract_num(sentenc),NumberToHanzi.dig2cn(_extract_num(sentenc)))
        else:
            return sentenc
        
    
    def _total_sentenc(self,sentenc):
        try:
            sentenc1=self._pinyin_sentenc(sentenc)
            # sentenc1=Traditional2Simplified(sentenc1)
            return sentenc1
        except Exception as e:
            return sentenc
        
    def text_correction(self,sentenc):
        result_sent=self._total_sentenc(sentenc)
        corrected_sent, detail = pycorrector.correct("".join(result_sent))
        return  corrected_sent

if __name__ == "__main__":
    sentenc='这个object给你了,keyi，我现在就打个，旭要1000万，憂郁的臺灣烏龜'
    print(TextCorrection().text_correction(sentenc))



