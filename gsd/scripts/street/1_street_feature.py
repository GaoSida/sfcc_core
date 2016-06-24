# coding:utf-8
# 为现有特征添加街道信息
# 首先，尝试使用总计数；然后尝试使用总计数的概率；最后尝试平均概率

import pickle
import numpy as np
import pandas as pd
import math

file_key = "train"

street_cnts = pickle.load(file('street_per_category_counts.pickle'))

original = pd.read_csv('../../../features/0_direct/' + file_key + '.csv')

for i in range(39):
    original['street_odds_' + str(i)] = 0

for i in range(len(original)):
    addresses = [0, 0]
    category = int(original.loc[i, 'Category'])
    addresses[0] = int(original.loc[i, 'Address1'])
    addresses[1] = int(original.loc[i, 'Address2'])

    for street in addresses:
        if street > 0:
            for j in range(39):
                # 计数时不算自己
                original.loc[i, 'street_odds_' + str(j)] += \
                     street_cnts[street][j] - int(j == category)

    crime_sum = 0
    for j in range(39):
        original.loc[i, 'street_odds_' + str(j)] += 1     # 平滑处理
        crime_sum += original.loc[i, 'street_odds_' + str(j)]

    # 转换成log odds
    for j in range(39):
        p = original.loc[i, 'street_odds_' + str(j)] / crime_sum
        original.loc[i, 'street_odds_' + str(j)] = math.log(1 / 1 - p)

    if i % 50000 == 0:
        print "done " + str(i)

original.to_csv('../../../features/' + file_key + '_street.csv', index=False)
