# -*- coding: utf-8 -*-
"""
@Software:spyder
@File:convertchar.py
@Created on Thu Jun  4 16:08:47 2020
@author: betty
@description:文本转拼音、提取文字、提取数字、提取字母、英中翻译
"""
import re
from translate import Translator

def _extract_character(char):
    # 提取文字
    return  re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", char)


def _extract_num(char):
    # 提取数字
    return re.sub("\D", "", char) 


def _extract_letter(char):
    # 提取字母
    return  ''.join(re.findall(r"[A-Za-z]", char)) 

def _chinese_to_english(char):
    #英文转中文
    translator= Translator(to_lang="chinese")
    return  translator.translate(char)

if __name__ == "__main__":
    print(_convert_pinyin('我们'))
    print(_extract_letter('我们一起去shopping'))
    print(_extract_num('我们一起去shopping,886'))
    print(_extract_character('我们一起去shopping,886'))
    print(_chinese_to_english('shopping and some other'))
    
    
