"""
@Software:spyder
@File:ConvertPinyin.py
@Created on Thu Jun  4 16:08:47 2020
@author: betty
@description:文本转拼音
"""

from xpinyin import Pinyin
p = Pinyin()
def _convert_pinyin(char):
    # 文本转拼音
    return  p.get_pinyin(char,' ')
if __name__ == "__main__":
    sentenc='我们'
    print(_convert_pinyin(sentenc))