# -*- coding: utf-8 -*-
"""
@Software:spyder
@File:PinYinChar.py
@Created on Thu Jun  4 16:08:47 2020
@author: betty
@description:拼音转文本
"""
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag
from pinyin_dict import all_list,removetone_dict
from operator import itemgetter





class PinYinChar():
    
    def __init__(self):
        self.__pinyin = set(all_list)
        self.__removetone_dict = removetone_dict
    
    def all_pinyin(self):
        for _ in self.__pinyin:
            yield _
    
    def remove_tone(self,one_py):
        """ 删除拼音中的音调
        lǔ -> lu
        """
        one_py = self.as_text(one_py)
        r = self.as_text('')
        for c in one_py:
            if c in self.__removetone_dict:
                r += self.__removetone_dict[c]
            else:
                r += c
        return r
    
    def as_text(self,v):  ## 生成unicode字符串
        if v is None:
            return None
        elif isinstance(v, bytes):
            return v.decode('utf-8', errors='ignore')
        elif isinstance(v, str):
            return v
        else:
            raise ValueError('Unknown type %r' % type(v))
            
    def py_result(self,result_list):
        for item in range(0,len(result_list)):
            item_list = list(result_list[item])
            num_list, res_list, num = [], [], 0
            for i in range(0, len(item_list)):
                one_py = item_list[i]
                num_list.append(one_py in self.__removetone_dict)
                if one_py in self.__removetone_dict:
                    res_list.append("%s、" % one_py)
                    num += 1
                else:
                    res_list.append("%s" % one_py)
            if num > 1:
                py_ok = ' '.join(''.join(res_list).split("、")[:-2])
                py_end_ok = ''.join(''.join(res_list).split("、")[-2:])
                py_res = "%s %s"%(py_ok, py_end_ok)
                result_list[item] = py_res
    
    def get_split_py(self,text):
        result_list = []
        py_text = self.remove_tone(text)
    
        def get_py(y):
            py_list = []
            for i in range(y, len(py_text) + 1):
                if y == 1:
                    y = y - 1
                nr = py_text[y:i]
                y_nr = text[y:i]
                if nr in self.all_pinyin():
                    py_list.append([y_nr,y,i])
            result = py_list[-1][0]
            if py_list[-1][2] < len(text):
                nr = py_text[py_list[-1][2]-1:py_list[-1][2]+1]
                anr = py_text[py_list[-1][2]:py_list[-1][2]+2]
                if nr in self.all_pinyin() and anr not in self.all_pinyin():
                    result = py_list[-2][0]
            return result
    
        py_str = get_py(1)
        while 1:
            result_list.append(py_str)
            num = len(''.join(result_list))
            if num < len(text):
                py_str = get_py(num)
            else:
                self.py_result(result_list)
                break
        return ' '.join(result_list)
    
    def pinyin_2_hanzi(self,pinyinList):
       dagParams = DefaultDagParams()
       result = dag(dagParams, pinyinList, path_num=10, log=True)#10代表侯选值个数
       item_result=[]
       try:
           for item in result:
               # socre = item.score 
               # res = item.path # 转换结果
               item_result.append([item.score,item.path])
           return  sorted(item_result, key=itemgetter(0),reverse=True)[0][1]
       except Exception as e:
           print(e)
           print("输入异常，请重新输入拼音")
    def pinyin_2_hanzi_output(self,pinyin):
        result_sent=self.pinyin_2_hanzi(self.get_split_py(pinyin).split(' '))
        return ''.join(result_sent)
if __name__ == "__main__":
    gg=PinYinChar()
    print(gg.pinyin_2_hanzi_output('shopping and buy some other '))
