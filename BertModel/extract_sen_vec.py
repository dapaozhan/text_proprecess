# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/5/8 20:04
# @author   :Mo
# @function :extract feature of bert and keras
import codecs
import warnings
warnings.filterwarnings('ignore')
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import keras.backend.tensorflow_backend as ktf_keras
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Add
from keras.models import Model
from keras_bert import load_trained_model_from_checkpoint, Tokenizer

from .layers_keras import NonMaskingLayer
from .conf import gpu_memory_fraction, config_name, ckpt_name, vocab_file, max_seq_len, layer_indexes

# 全局使用，使其可以django、flask、tornado等调用
graph = None
model = None
# gpu配置与使用率设置
# os.environ['CUDA_VISIBLE_DEVICES'] = '0'
config = tf.compat.v1.ConfigProto(allow_soft_placement=True)
# config.gpu_options.per_process_gpu_memory_fraction = gpu_memory_fraction
sess = tf.compat.v1.Session(config=config)  #注意 ，这里为tensorflow2.0版本，与第1.0有差距。ktf_keras.set_session (sess)


class KerasBertVector ():
    def __init__(self):
        self.config_path, self.checkpoint_path, self.dict_path, self.max_seq_len = config_name, ckpt_name, vocab_file, max_seq_len
        # 全局使用，使其可以django、flask、tornado等调用
        # global graph
        # graph = tf.compat.v1.get_default_graph ()
        global model
        model = load_trained_model_from_checkpoint (self.config_path, self.checkpoint_path,
                                                    seq_len=self.max_seq_len)
        # print (model.output)
        # print (len (model.layers))
        # lay = model.layers
        # 一共104个layer，其中前八层包括token,pos,embed等，
        # 每4层（MultiHeadAttention,Dropout,Add,LayerNormalization）
        # 一共24层
        layer_dict = [7]
        layer_0 = 7
        for i in range (12):
            layer_0 = layer_0 + 4
            layer_dict.append (layer_0)
        # 输出它本身
        if len (layer_indexes) == 0:
            encoder_layer = model.output
        # 分类如果只有一层，就只取最后那一层的weight，取得不正确
        elif len (layer_indexes) == 1:
            if layer_indexes[0] in [i + 1 for i in range (12)]:
                encoder_layer = model.get_layer (index=layer_dict[layer_indexes[0]]).output
            else:
                encoder_layer = model.get_layer (index=layer_dict[-2]).output
        # 否则遍历需要取的层，把所有层的weight取出来并拼接起来shape:768*层数
        else:
            # layer_indexes must be [1,2,3,......12...24]
            # all_layers = [model.get_layer(index=lay).output if lay is not 1 else model.get_layer(index=lay).output[0] for lay in layer_indexes]
            all_layers = [model.get_layer (index=layer_dict[lay - 1]).output if lay in [i + 1 for i in range (12)]
                          else model.get_layer (index=layer_dict[-1]).output  # 如果给出不正确，就默认输出最后一层
                          for lay in layer_indexes]
            # print (layer_indexes)
            # print (all_layers)
            # 其中layer==1的output是格式不对，第二层输入input是list
            all_layers_select = []
            for all_layers_one in all_layers:
                all_layers_select.append (all_layers_one)
            encoder_layer = Add () (all_layers_select)
            # print (encoder_layer.shape)
        # print ("KerasBertEmbedding:")
        # print (encoder_layer.shape)
        output_layer = NonMaskingLayer () (encoder_layer)
        model = Model (model.inputs, output_layer)
        # model.summary(120)
        # reader tokenizer
        self.token_dict = {}
        with codecs.open (self.dict_path, 'r', 'utf8') as reader:
            for line in reader:
                token = line.strip ()
                self.token_dict[token] = len (self.token_dict)

        self.tokenizer = Tokenizer (self.token_dict)

    def bert_encode_sen(self, texts):
        # 文本预处理
        input_ids = []
        input_masks = []
        input_type_ids = []
        for text in texts:
            # print (text)
            tokens_text = self.tokenizer.tokenize (text)
            # print ('Tokens:', tokens_text)
            input_id, input_type_id = self.tokenizer.encode (first=text, max_len=self.max_seq_len)
            input_mask = [0 if ids == 0 else 1 for ids in input_id]
            input_ids.append (input_id)
            input_type_ids.append (input_type_id)
            input_masks.append (input_mask)

        input_ids = np.array (input_ids)
        input_masks = np.array (input_masks)
        input_type_ids = np.array (input_type_ids)

        # 全局使用，使其可以django、flask、tornado等调用
        # with graph.as_default ():
        predicts = model.predict ([input_ids, input_type_ids], batch_size=1)
        # print (predicts.shape)
        # for i, token in enumerate (tokens_text):
        #     (token, [len (predicts[0][i].tolist ())], predicts[0][i].tolist ())

        # 相当于pool，采用的是https://github.com/terrifyzhao/bert-utils/blob/master/graph.py
        mul_mask = lambda x, m: x * np.expand_dims (m, axis=-1)
        masked_reduce_mean = lambda x, m: np.sum (mul_mask (x, m), axis=1) / (np.sum (m, axis=1, keepdims=True) + 1e-9)

        pools = []
        for i in range (len (predicts)):
            pred = predicts[i]
            masks = input_masks.tolist ()
            mask_np = np.array ([masks[i]])
            pooled = masked_reduce_mean (pred, mask_np)
            pooled = pooled.tolist ()
            pools.append (pooled[0])
        # print ('bert:', pools)
        return pools

    def bert_encode_word(self, texts):
        # 文本预处理
        input_ids = []
        input_masks = []
        input_type_ids = []
        for text in texts:
            # print (text)
            tokens_text = self.tokenizer.tokenize (text)
            # print ('Tokens:', tokens_text)
            input_id, input_type_id = self.tokenizer.encode (first=text, max_len=self.max_seq_len)
            input_mask = [0 if ids == 0 else 1 for ids in input_id]
            input_ids.append (input_id)
            input_type_ids.append (input_type_id)
            input_masks.append (input_mask)

        input_ids = np.array (input_ids)
        input_masks = np.array (input_masks)
        input_type_ids = np.array (input_type_ids)

        # 全局使用，使其可以django、flask、tornado等调用
        # with graph.as_default ():
        predicts = model.predict ([input_ids, input_type_ids], batch_size=1)
        # print (predicts.shape)
        # for i, token in enumerate (tokens_text):
        #     (token, [len (predicts[0][i].tolist ())], predicts[0][i].tolist ())
        words_vec=predicts[0][1:len(tokens_text)-1]
        words_vec = np.array (words_vec)
        words_vec = (words_vec.astype (np.float32))
        ret=[]
        for i in words_vec:
            ret.append(i)
        return ret
    def gen_sen_vec(self,sen):
        pooled = self.bert_encode_sen([sen])
        vec = pooled[0]
        vec = np.array (vec)
        vec.tolist ()
        return vec
    def gen_words_vec(self,sen):
        pooled = self.bert_encode_word ([sen])
        vec = pooled[0]
        vec = np.array (vec)
        vec.tolist ()
        return vec
if __name__ == "__main__":

    bert_vector = KerasBertVector ()
    bert_vector.gen_words_vec('后天')
    bert_vector.gen_sen_vec('我今天要去上班')
    len(bert_vector.gen_sen_vec('我觉得我今天必须要购物'))

#
# vec=gen_sen_vec('how are you')
# vec=np.array(vec)
# print(vec)
# vec=(vec.astype(np.float64))
# vec.tolist()
# print(vec)
    # print (pooled)
    # while True:
    #     print ("input:")
    #     ques = input ()
    #     print (bert_vector.bert_encode ([ques]))
