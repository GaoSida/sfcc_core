# coding:utf-8
# 统计一共有多少种地址

import pandas as pd
import numpy as np

train = pd.read_csv('../../data/train.csv')
test = pd.read_csv('../../data/test.csv')

address_cnt = {}

for addr in train['Address'].values:
    if addr in address_cnt:
        address_cnt[addr] += 1
    else:
        address_cnt[addr] = 1

for addr in test['Address'].values:
    if addr in address_cnt:
        address_cnt[addr] += 1
    else:
        address_cnt[addr] = 1

print len(address_cnt)

cnts = []
for addr in address_cnt.keys():
    cnts.append(address_cnt[addr])
sorted_cnts = np.sort(cnts)
print sorted_cnts[1000]
print pd.DataFrame(cnts).describe()


