# coding:utf-8
# 把街道按照上面发生的所有犯罪的分布进行编码

import pandas as pd
import numpy as np
import pickle

file_key = 'fold_1'
original_train = pd.read_csv('../0_direct/' + file_key + '.csv')

# 统计各个街道上面各类犯罪的分布，街道编号由1到2128
street_stats = []
for i in range(2129):
    street_stats.append(np.zeros(40))

for i in range(len(original_train)):
    addresses = [0, 0]
    addresses[0] = int(original_train.loc[i, 'Address1'])
    addresses[1] = int(original_train.loc[i, 'Address2'])

    category = int(original_train.loc[i, 'Category'])

    for street in addresses:
        if street > 0:
            street_stats[street][category] += 1

    if (i % 20000 == 0):
        print i

pickle.dump(street_stats, file('street_counts' + file_key + '.pickle', 'w'))