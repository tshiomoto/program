# -*- coding: utf-8 -*-

import numpy as np

from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F

class BaseCNN(nn.Module):

    def __init__():
        super(VGG_128, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, 5, stride=1)
        self.pool1 = nn.MaxPool2d(3, stride=2)

        self.conv2 = nn.Conv2d(32, 32, 5, stride=1)
        self.pool2 = nn.AveragePool2d(3, stride=2)

        self.conv3 = nn.Conv2d(32, 64, 5, stride=1)
        self.pool3 = nn.AveragePool2d(3, stride=2)

        self.fc4 = nn.Linear(64 * 3 * 3, 500)
        self.fc5 = nn.Linear(500, 64)


    def forward(self, x):
        h1 = self.pool1(F.relu(self.conv1(x)))
        h2 = self.pool2(F.relu(self.conv2(h1)))
        h3 = self.pool3(F.relu(self.conv3(h2)))
        h4 = F.relu(self.fc4(h3))
        output = self.fc5(h4)

        return output