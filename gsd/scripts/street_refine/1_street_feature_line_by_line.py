# coding:utf-8
# 为现有特征添加街道信息
# 首先，尝试使用总计数；然后尝试使用总计数的概率；最后尝试平均概率

import pickle
import numpy as np
import pandas as pd
import math

file_key = "test"

street_cnts = pickle.load(file('street_per_category_counts.pickle'))

original = pd.read_csv('../../../features/0_direct/' + file_key + '.csv')
target = file('../../../features/street_' + file_key + '.csv', 'w')

for i in range(39):
    target.write('street_odds_' + str(i) + ',')
target.write('\n')

for i in range(len(original)):
    addresses = [0, 0]
    if (file_key == "train"):
        category = int(original.loc[i, 'Category'])
    else:
        category = -101
    addresses[0] = int(original.loc[i, 'Address1'])
    addresses[1] = int(original.loc[i, 'Address2'])

    crime_cnt = np.zeros(39)
    for street in addresses:
        if street > 0:
            for j in range(39):
                # 计数时不算自己
                crime_cnt[j] += street_cnts[street][j] - int(j == category)

    crime_sum = 0
    for j in range(39):
        crime_cnt[j] += 1     # 平滑处理
        crime_sum += crime_cnt[j]

    # 转换成log odds
    for j in range(39):
        p = 1.0 * crime_cnt[j] / crime_sum
        target.write(str(math.log(p / (1 - p))) + ',')
    target.write('\n')

    if i % 10000 == 0:
        print "done " + str(i)
