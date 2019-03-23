# -*- coding: utf-8 -*-

import numpy as np

import torch
import torchvision
import torchvision.transforms as transforms

data_path = '../data/cifar10/'

def data_read_train():
    train_path = data_path + 'train'

    transform = transforms.Compose(
    [transforms.ToTensor(), 
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    trainset = torchvision.datasets.CIFAR10(root=train_path, train=True,
                                        download=True, transform=transform)
    
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                          shuffle=True, num_workers=2)



def data_read_test():
    test_path = data_path + 'test'

    transform = transforms.Compose(
    [transforms.ToTensor(), 
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    testset = torchvision.datasets.CIFAR10(root=test_path, train=False,
                                        download=True, transform=transform)
    
    testloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                          shuffle=False, num_workers=2)  