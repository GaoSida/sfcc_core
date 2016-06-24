# coding:utf-8
# 把街道按照上面发生的所有犯罪的分布进行编码

import pandas as pd
import numpy as np
import pickle

original_train = pd.read_csv('../../../features/0_direct/train.csv')

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

print street_stats[2128]
print street_stats[1000]


pickle.dump(street_stats, file('street_per_category_counts.pickle', 'w'))


