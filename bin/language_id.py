# -*- coding: utf-8 -*-
"""
@Software:spyder
@File:PinYinChar.py
@Created on Thu Jun  4 16:08:47 2020
@author: betty
@description:语种识别
"""
import langid
def language_id(char):
    return langid.classify(char)
    