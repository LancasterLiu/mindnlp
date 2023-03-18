# model
# LancasterLiu
# 2023/3/8
"""MindNLP Roberta model"""
import mindspore.numpy as mnp
import mindspore.common.dtype as mstype
from mindspore import nn
from mindspore import ops
from mindspore import Parameter, Tensor
from mindspore.common.initializer import initializer, TruncatedNormal
from mindnlp._legacy.nn import Dropout


""" 
__all__ = [
     'RobertaEmbeddings', 'RobertaAttention', 'RobertaEncoder', 'RobertaIntermediate', 'RobertaLayer',
    'RobertaModel', 'RobertaForPretraining', 'RobertaLMPredictionHead'
]
"""