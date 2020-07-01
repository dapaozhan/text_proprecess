### 该代码结构为

    D:\NLP_CHARDEAL
    │  convert_pinyin.py    #将中文转为拼音
    │  language_id.py       #语种识别
    │  NumberToHanzi.py     #数字转汉字
    │  PinYinChar.py        #拼音转中文
    │  pinyin_dict.py       #拼音映射表
    │  TextCorrection.py    #文本纠错
    │
    ├─BertModel             #基于bert转词向量
      │  conf.py            #配置信息
      │  extract_sen_vec.py #主程序，主要转词向量则导入该代码
      │  layers_keras.py    #创建keras-bert模型
      │  readme.md          
      │
      │
      └─chinese_L-12_H-768_A-12 #bert中文模型
                bert_config.json
                bert_model.ckpt.data-00000-of-00001
                bert_model.ckpt.index
                bert_model.ckpt.meta
                vocab.txt
### 该代码满足的功能有：

1、文本转拼音
```python
import os 
os.chdir(r'D:\pycharmcode\GreeNLP\apps\textPreprocess\apps')
from src.ConvertPinyin import _convert_pinyin
print(_convert_pinyin('我们'))
Out[26]:wo men
```
2、提取英文字段
```python
from src.convert_pinyin import _extract_letter
_extract_letter('我们一起去shopping')

Out[26]: 'shopping'
```
3、提取数字
```python
from src.convert_pinyin import _extract_num
_extract_num('我们一起去shopping,886')

Out[28]: '886'
```
4、提取中文字符
```python
from convert_pinyin import _extract_character
_extract_character('我们一起去shopping,886')

Out[29]: '我们一起去'
```
5、英文转中文
```python
from src.convert_pinyin import _chinese_to_english
_chinese_to_english('shopping and some other')

Out[30]: '购物和其他'
```

6、字符型的数字转中文的数字表示

```python
from src.NumberToHanzi import NumberToHanzi
nt=NumberToHanzi()
nt.dig2cn('5555')

Out[45]: '五千五百五十五'
```

7、拼音转文本
```python
from src.PinYinChar import PinYinChar 
pyc=PinYinChar()
pyc.pinyin_2_hanzi_output('womenyiqi')

Out[53]: '我们一起'
```


8、文本纠错
```python
from src.TextCorrection import TextCorrection
sentenc='这个object就交给你了，我旭要1000万'
print(TextCorrection().text_correction(sentenc))

Out[62]: '这个对象就交给你了,我需要一千万'
```

9、基于bert转词向量
```python
from BertModel.extract_sen_vec import KerasBertVector
bert_vector=KerasBertVector()
bert_vector.gen_words_vec('后天')#1*768维
Out[68]: 
array([-4.53199670e-02,  4.20343399e-01, -1.44934964e+00, -1.92995816e-01,
        5.12931406e-01, -8.32412899e-01,  1.80846226e+00, -2.24694580e-01,
       -3.21841985e-02,  1.13120818e+00, -2.98911631e-01,  8.11511874e-01,
        。。。。。。。。。
        1.02704155e+00,  5.30606151e-01, -4.79678482e-01, -8.11019987e-02],
      dtype=float32)
```

10、基于bert转句向量

```python
from BertModel.extract_sen_vec import KerasBertVector
bert_vector=KerasBertVector()
bert_vector.gen_sen_vec('我今天要去上班')#1*768维
Out[69]: 
array([ 2.18004545e-01,  2.25322694e-03, -1.57206805e-01,  2.24931460e-01,
       -2.39904237e-01, -9.45290335e-01,  2.37803559e-01, -6.38593530e-01,
       -4.85544162e-01,  1.44703646e-01,  4.11843856e-01, -6.72831697e-01,
       -2.96609055e-01, -2.13621430e-01,  1.46656836e+00, -5.80576977e-02,
        5.97117969e-01,  1.93033026e-01,  2.77227563e-01, -1.34612085e-01,
        。。。。。。。。。。。
       -2.60482280e+01, -8.45735988e-02, -8.96670752e-03,  5.83095054e-02,
       -3.89684952e-01,  5.20540264e-01, -1.93629252e-01,  9.10033004e-02,
        2.96961958e-01, -1.53515632e-01, -1.04824003e-01,  1.92818124e-01])
```
11、繁体字转简体
```python
from src.LangConv import Traditional2Simplified
traditional_sentence = '憂郁的臺灣烏龜'
print(Traditional2Simplified(traditional_sentence))
Out[69]: 忧郁的台湾乌龟
```
12、中文数字转阿拉伯数字
```python
from src.ChineseToArabic import chinese_to_arabic
print(chinese_to_arabic('五百二十'))
Out[69]:520
```
### 需要的包以及版本

| 包名      | 版本 |
| --------- | -----:|
| pyhanlp  |  0.1.66 |
| translate     |   3.5.0 |
| langid      |    1.1.6 |
| Pinyin2Hanzi  |  0.1.1 |
| pycorrector     |  0.2.8 |
| tensorflow      |    2.0.0  |
| Keras  |   2.3.1  |
| xpinyin     |  0.5.6  |
| jieba      |     0.42.1  |
| translate      |      3.5.0  |

微信公众号：屁屁和铭仔的数据之路
