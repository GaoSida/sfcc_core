# coding:utf-8
# 为现有特征添加街道信息
# 首先，尝试使用总计数；然后尝试使用总计数的概率；最后尝试平均概率

import pickle
import numpy as np
import pandas as pd
import math

file_key = "fold_0"
anti_file_key = "fold_1"

street_cnts = pickle.load(file('street_counts' + anti_file_key + '.pickle'))

original = pd.read_csv('../0_direct/' + file_key + '.csv')
target = file('../features/street_redo_' + file_key + '.csv', 'w')

for i in range(39):
    target.write('street_odds_' + str(i))
    if i == 38:
        target.write('\n')
    else:
        target.write(',')

for i in range(len(original)):
    addresses = [0, 0]
    '''
    if (file_key == "train"):
        category = int(original.loc[i, 'Category'])
    else:
        category = -101
    '''
    addresses[0] = int(original.loc[i, 'Address1'])
    addresses[1] = int(original.loc[i, 'Address2'])

    crime_cnt = np.zeros(39)
    for street in addresses:
        if street > 0:
            for j in range(39):
                # 计数时不算自己
                crime_cnt[j] += street_cnts[street][j]

    crime_sum = 0
    for j in range(39):
        crime_cnt[j] += 1     # 平滑处理
        crime_sum += crime_cnt[j]

    # 转换成log odds
    for j in range(39):
        p = 1.0 * crime_cnt[j] / crime_sum
        target.write(str(math.log(p / (1 - p))))
        if j == 38:
            target.write('\n')
        else:
            target.write(',')

    if i % 10000 == 0:
        print "done " + str(i)
