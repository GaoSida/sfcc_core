# coding:utf-8
# 计算精确地址的分布，做平滑

import pandas as pd
import numpy as np

train = pd.read_csv('/Users/gaosida/desktop/train_originaladdr.csv')
test = pd.read_csv('/Users/gaosida/desktop/test_originaladdr.csv')

address_cnt = {}
train_address = train['Original_Addr'].values
train_labels = train['Category'].values

for i in range(len(train)):
    addr = train_address[i]
    cata = train_labels[i]
    if addr in address_cnt:
        address_cnt[addr][cata] += 1
    else:
        address_cnt[addr] = np.zeros(39)

# 平滑
for addr in address_cnt:
    for i in range(39):
        address_cnt[addr][i] += 1

# 加的特征
for i in range(39):
    train['addr_' + str(i)] = 0
    test['addr_' + str(i)] = 0

for i in range(len(train)):
    addr = train_address[i]
    cata = train_labels[i]
    for j in range(39):
        train.loc[i, 'addr_' + str(j)] = address_cnt[addr][j] - int(j == cata)
train.to_csv('/Users/gaosida/desktop/train_addr.csv', index=False)

for i in range(len(test)):
    addr = test_address[i]
    for j in range(39):
        test.loc[i, 'addr_' + str(j)] = address_cnt[addr][j]
test.to_csv('/Users/gaosida/desktop/test_addr.csv', index=False)










