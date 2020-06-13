# -*- coding: utf-8 -*-
"""
@Software:spyder
@File:NumberToHanzi.py
@Created on Thu Jun  4 16:08:47 2020
@author: betty
@description:数字转文本表达
"""

class NumberToHanzi():
    def __init__(self):

        self.han_list = ["零" , "一" , "二" , "三" , "四" , "五" , "六" , "七" , "八" , "九"]
        self.unit_list = ["十" , "百" , "千"]
    '''
      把一个四位的数字字符串变成汉字字符串
      num_str 需要被转换的四位的数字字符串
      返回四位的数字字符串被转换成汉字字符串
    '''
    def four_to_hanstr(self,num_str):
        result = ""
        num_len = len(num_str)
        for i in range(num_len):
            num = int(num_str[i])
            if i != num_len - 1 and num != 0 :
                result += self.han_list[num] + self.unit_list[num_len - 2 - i]
            else :
                if num == 0 and result and result[-1]=='零':
                    continue
                else:
                    result += self.han_list[num]
        return result

    def dig2cn(self,num_str):
        str_len = len(num_str)
        if str_len > 12 :
            print('数字太大，翻译不了')
            return
        # 如果大于8位，包含单位亿
        elif str_len > 8:
            hanstr = self.four_to_hanstr(num_str[:-8]) + "亿" + \
                self.four_to_hanstr(num_str[-8: -4]) + "万" + \
                self.four_to_hanstr(num_str[-4:])
        # 如果大于4位，包含单位万
        elif str_len > 4:
            hanstr = self.four_to_hanstr(num_str[:-4]) + "万" + \
                self.four_to_hanstr(num_str[-4:])
        else:
            hanstr = self.four_to_hanstr(num_str)

        if hanstr[-1]=='零':
            hanstr = hanstr[:-1]
        return hanstr
if __name__ == "__main__":
    gg=NumberToHanzi()
    print(gg.dig2cn('5555'))
