"""
@Software:spyder
@File:pinyin_dict.py
@Created on Thu Jun  4 16:08:47 2020
@author: betty
@description:拼音转文本映射关系
"""

all_list = ['gu','qiao','qian','qve','ge','gang','ga','lian','liao','rou','zong',\
    'tu','seng','yve','ti','te','jve','ta','nong','zhang','fan','ma','gua','die','gui',\
    'guo','gun','sang','diu','zi','ze','za','chen','zu','ba','dian','diao','nei','suo',\
    'sun','zhao','sui','kuo','kun','kui','cao','zuan','kua','den','lei','neng','men',\
    'mei','tiao','geng','chang','cha','che','fen','chi','fei','chu','shui','me','tuan',\
    'mo','mi','mu','dei','cai','zhan','zhai','can','ning','wang','pie','beng','zhuang',\
    'tan','tao','tai','song','ping','hou','cuan','lan','lao','fu','fa','jiong','mai',\
    'xiang','mao','man','a','jiang','zun','bing','su','si','sa','se','ding','xuan',\
    'zei','zen','kong','pang','jie','jia','jin','lo','lai','li','peng','jiu','yi','yo',\
    'ya','cen','dan','dao','ye','dai','zhen','bang','nou','yu','weng','en','ei','kang',\
    'dia','er','ru','keng','re','ren','gou','ri','tian','qi','shua','shun','shuo','qun',\
    'yun','xun','fiao','zan','zao','rang','xi','yong','zai','guan','guai','dong','kuai',\
    'ying','kuan','xu','xia','xie','yin','rong','xin','tou','nian','niao','xiu','fo',\
    'kou','niang','hua','hun','huo','hui','shuan','quan','shuai','chong','bei','ben',\
    'kuang','dang','sai','ang','sao','san','reng','ran','rao','ming','tei','lie','lia',\
    'min','pa','lin','mian','mie','liu','zou','miu','nen','kai','kao','kan','ka','ke',\
    'yang','ku','deng','dou','shou','chuang','nang','feng','meng','cheng','di','de','da',\
    'bao','gei','du','gen','qu','shu','sha','she','ban','shi','bai','nun','nuo','sen','lve',\
    'kei','fang','teng','xve','lun','luo','ken','wa','wo','ju','tui','wu','le','ji','huang',\
    'tuo','cou','la','mang','ci','tun','tong','ca','pou','ce','gong','cu','lv','dun','pu',\
    'ting','qie','yao','lu','pi','po','suan','chua','chun','chan','chui','gao','gan','zeng',\
    'gai','xiong','tang','pian','piao','cang','heng','xian','xiao','bian','biao','zhua','duan',\
    'cong','zhui','zhuo','zhun','hong','shuang','juan','zhei','pai','shai','shan','shao','pan',\
    'pao','nin','hang','nie','zhuai','zhuan','yuan','niu','na','miao','guang','ne','hai','han',\
    'hao','wei','wen','ruan','cuo','cun','cui','bin','bie','mou','nve','shen','shei','fou','xing',\
    'qiang','nuan','pen','pei','rui','run','ruo','sheng','dui','bo','bi','bu','chuan','qing',\
    'chuai','duo','o','chou','ou','zui','luan','zuo','jian','jiao','sou','wan','jing','qiong',\
    'wai','long','yan','liang','lou','huan','hen','hei','huai','shang','jun','hu','ling','ha','he',\
    'zhu','ceng','zha','zhe','zhi','qin','pin','ai','chai','qia','chao','ao','an','qiu','ni','zhong',\
    'zang','nai','nan','nao','chuo','tie','you','nu','nv','zheng','leng','zhou','lang','e','jue','xue',\
    'yue','eng','lue','nue','que','rua']
removetone_dict = {
    'ā': 'a',
    'á': 'a',
    'ǎ': 'a',
    'à': 'a',
    'ē': 'e',
    'é': 'e',
    'ě': 'e',
    'è': 'e',
    'ī': 'i',
    'í': 'i',
    'ǐ': 'i',
    'ì': 'i',
    'ō': 'o',
    'ó': 'o',
    'ǒ': 'o',
    'ò': 'o',
    'ū': 'u',
    'ú': 'u',
    'ǔ': 'u',
    'ù': 'u',
    'ü': 'v',
    'ǖ': 'v',
    'ǘ': 'v',
    'ǚ': 'v',
    'ǜ': 'v',
    'ń': 'n',
    'ň': 'n',
    '': 'm',
}