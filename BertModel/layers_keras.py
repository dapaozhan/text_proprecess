# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/5/10 10:49
# @author   :Mo
# @function :create model of keras-bert for get [-2] layers
from keras.engine import Layer
class NonMaskingLayer (Layer):
    """
    fix convolutional 1D can't receive masked input, detail: https://github.com/keras-team/keras/issues/4978
    thanks for https://github.com/jacoxu
    """

    def __init__(self, **kwargs):
        self.supports_masking = True
        super (NonMaskingLayer, self).__init__ (**kwargs)

    def build(self, input_shape):
        pass

    def compute_mask(self, input, input_mask=None):
        # do not pass the mask to the next layers
        return None

    def call(self, x, mask=None):
        return x

    def compute_output_shape(self, input_shape):
        return input_shape