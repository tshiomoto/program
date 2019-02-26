# -*- coding: utf-8 -*-

import numpy as np
import argparse

from torch.autograd import Variable
import torch.nn as nn

from model.base_cnn import BaseCNN
import model.encode as encode

data_path = 'data/cifar10'

def parse_argument():
    parser = argparse.ArgumentParser(
        prog="train.py",
        usage="python train.py [-h help | -o, --onehot onehot | -d, --divide_num divide_num | -i, --iteration iteration ] [arg] ...",
        add_help=True
    )

    parser.add_argument(
        '-o', '--onehot',
        help="decides length of subvectors",
        required=True,
        type=int
    )

    parser.add_argument(
        '-d', '--divide_num',
        help="decides how many numbers you divide main vector into subvectors",
        required=True,
        type=int
    )

    parser.add_argument(
        '-i', '--iteration',
        help="training iteration number",
        required=False,
        type=int,
        default=1000
    )

    args = parser.parse_args()
    return args

def train(onehot, devide_num, iteration):
    train_data = data_read_train(data_path)
    base = BaseCNN(onehot=onehot, divide_num=devide_num)

    for ite_num in range(iteration):
        pass

def data_read_train(path):

if __name__ == '__main__':
    args = parse_argument()
    train(args.onehot, args.divide_num, args.iteration)