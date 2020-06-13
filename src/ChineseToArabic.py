"""
@Software:spyder
@File:ChineseToArabic.py
@Created on Thu Jun  4 16:08:47 2020
@author: betty
@description:中文转数字
"""
from  bin.num_dict import CN_NUM,CN_UNIT
def chinese_to_arabic(cn:str) -> int:
    unit = 0   # current
    ldig = []  # digest
    for cndig in reversed(cn):
        if cndig in CN_UNIT:
            unit = CN_UNIT.get(cndig)
            if unit == 10000 or unit == 100000000:
                ldig.append(unit)
                unit = 1
        else:
            dig = CN_NUM.get(cndig)
            if unit:
                dig *= unit
                unit = 0
            ldig.append(dig)
    if unit == 10:
        ldig.append(10)
    val, tmp = 0, 0
    for x in reversed(ldig):
        if x == 10000 or x == 100000000:
            val += tmp * x
            tmp = 0
        else:
            tmp += x
    val += tmp
    return val
if __name__ == "__main__":
    print (chinese_to_arabic('五百二十') )
    print (chinese_to_arabic('一亿零一'))