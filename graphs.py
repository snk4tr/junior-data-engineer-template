import torch.nn as nn


def get_mnist_net(config: dict):
    return nn.Sequential(nn.Linear(784, 128),
                         nn.ReLU(),
                         nn.Linear(128, 64),
                         nn.ReLU(),
                         nn.Linear(64, 10),
                         nn.LogSoftmax(dim=1))
