# -*- coding: utf-8 -*-

import numpy as np

from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F

def slice_vector(output_cnn, onehot):
    sliced = output_cnn[::onehot]
    return sliced