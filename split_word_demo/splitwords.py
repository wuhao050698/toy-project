# -*- coding: utf-8 -*-
import sys
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from datetime import datetime

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
torch.manual_seed(1)


# These will usually be more like 32 or 64 dimensional.
# We will keep them small, so we can see how the weights change as we train.
EMBEDDING_DIM = 20  # 词嵌入维度
HIDDEN_DIM = 40  # 隐藏层数量

SENT_LEN = 50
LSTM_LN = 2
INF = 10000

START_TAG = "<START>"
STOP_TAG = "<STOP>"
def