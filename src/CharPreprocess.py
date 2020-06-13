"""
@Software:spyder
@File:CharPreprocess.py
@Created on Thu Jun  4 16:08:47 2020
@author:
@description:中文转数字
"""
import jieba
def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

def is_number(uchar):
    """判断一个unicode是否是数字"""
    if uchar >= u'\u0030' and uchar <= u'\u0039':
        return True
    else:
        return False

def is_alphabet(uchar):
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False
def format_str(content):
    content_str = ''
    for i in content:
        if is_chinese(i)or is_number(i) or is_alphabet(i):
            content_str = content_str+i
    # content_str = TraditionalToSimplified(content_str)
    return content_str
if __name__ == '__main__':
    format_str('我今天遇到了mary,他跟我说她有10000万哦，我觉得好不可思议哦！')