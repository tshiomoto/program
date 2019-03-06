# -*- coding: utf-8 -*-

import numpy as np

from torch.autograd import Variable
import torch
import torch.nn as nn
import torch.nn.functional as F


batch_num = 64

'''
サブベクトルに分割するメソッド
input
    output_cnn: CNNから出力された特徴量ベクトル
    onehot: サブベクトルの長さ
    divide_num: サブベクトルの分割数
output
    output_cnnを[batch_num, onehot, divide_num]に変形したデータ
'''
def slice_vector(output_cnn, onehot, divide_num):
    return output_cnn.reshape([batch_num, onehot, divide_num])


'''
softmaxを計算するメソッド
input
    data: output_cnnを[batch_num, onehot, divide_num]に変形したデータ
output
    dataをonehot方向でsoftmax関数かけたデータ
'''
def b_softmax(data):
    softmax = F.softmax(dim=1)
    return softmax(data)


'''
log_softmaxを計算するメソッド
input
    data: output_cnnを[batch_num, onehot, divide_num]に変形したデータ
output
    dataをonehot方向でlog_softmax関数かけたデータ
'''
def b_log_softmax(data):
    log_softmax = F.log_softmax(dim=1)
    return log_softmax(data)

'''
onehotベクトルを生成するメソッド
input
    data: output_cnnを[batch_num, onehot, divide_num]に変形したデータ
output
    dataをonehot方向でonehotベクトルにしたかけたデータ
'''
def make_onehot_vector(data):
    predict_index_vector = torch.argmax(b_softmax(data), dim=1)
    onehot_vector = torch.Tensor(np.zeros_like(data))

    for index in range(data.shape[0]):
        predict_index_vector[index, onehot_vector[index]] = 1.

    return onehot_vector

'''
blockwise_entropyを計算するメソッド
input
    data: output_cnnを[batch_num, onehot, divide_num]に変形したデータ
output
    entropy: [batch_num, divide_num]のデータ，onehot方向にエントロピーを計算した値
'''
def blockwise_entropy(data):
    entropy = b_softmax(data) * b_log_softmax(data)
    entropy = -1.0 * entropy.sum(dim=0)
    return entropy

'''
1データごと全部のblockwise_entropyを計算し，その和を計算するメソッド
input
    data: output_cnnを[batch_num, onehot, divide_num]に変形したデータ
output
    dataごとのblockwise_entropyの和を計算する
'''
def tilde_entropy(data):
    entropy_vector = blockwise_entropy(data)
    return entropy_vector.sum(axis=1)

'''
バッチデータ全部のentropyを計算するメソッド
input
    data: output_cnnを[batch_num, onehot, divide_num]に変形したデータ
output
    バッチデータ全部のblockwise_entropyの和を計算する
'''
def bar_entropy(data):
    return F.mean(tilde_entropy(data))


class LinearClassification(nn.Module):

    def __init__(self):
        super(LinearClassification, self).__init__()
        self.fc = nn.Linear(1000, 100)


    def __call__(self, x):
        self.forward(x)

    def forward(self, x):
        return F.softmax(self.fc(x))