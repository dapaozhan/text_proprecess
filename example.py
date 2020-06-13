# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 10:38:31 2020

@author: 560350
"""
import os
os.chdir(r'D:\pycharmcode\GreeNLP\apps\textPreprocess\apps')
from src.ConvertPinyin import _convert_pinyin
print(_convert_pinyin('我们'))



import os
os.chdir(r'D:\nlp_chardeal')
from convert_pinyin import _convert_pinyin
print(_convert_pinyin('我们'))

from convert_pinyin import _extract_letter
_extract_letter('我们一起去shopping')

from convert_pinyin import _extract_num
_extract_num('我们一起去shopping,886')

from convert_pinyin import _extract_character
_extract_character('我们一起去shopping,886')



from convert_pinyin import _chinese_to_english
_chinese_to_english('shopping and some other')


from NumberToHanzi import NumberToHanzi
nt=NumberToHanzi()
nt.dig2cn('5555')


from PinYinChar import PinYinChar
pyc=PinYinChar()
pyc.pinyin_2_hanzi_output('womenyiqi')


import time

from TextCorrection import TextCorrection
start = time.time()
for k in range(100):
    sentenc='这个object给你了,我现在就打个，旭要1000万,憂郁的臺灣烏龜'
    TextCorrection().text_correction(sentenc)
end = time.time()
running_time = end-start
print('time cost : %.5f sec' %running_time)




from BertModel.extract_sen_vec import KerasBertVector
bert_vector=KerasBertVector()
bert_vector.gen_sen_vec('我今天要去上班')


from src.LangConv import Traditional2Simplified
traditional_sentence = '憂郁的臺灣烏龜'
print(Traditional2Simplified(traditional_sentence))



from src.CharPreprocess import format_str
print(format_str('我今天遇到了mary,他跟我说她有10000万哦，我觉得好不可思议哦！'))



