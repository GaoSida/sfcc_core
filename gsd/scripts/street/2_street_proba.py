# coding:utf-8
# 把计数形式的街道，改成比例形式

import pickle
import numpy as np
import pandas as pd

street_cnts = pickle.load(file('street_per_category_counts.pickle'))

original = file('../../../features/0_direct/train.csv')
target = file('../../../features/2_street/train.csv', 'w')

line_cnt = 0
for line in original:
    target.write(line[:-1])
    if line[0] == 'C':
    #if line[0] == 'I':
        for i in range(40):
            target.write(',street_proba_' + str(i))
        target.write(',street_sum\n')
    else:
        line = line.split(',')
        addresses = [0, 0]
        addresses[0] = int(line[9])
        addresses[1] = int(line[10])

        cnts = np.zeros(40)
        cnt_sum = 0

        for street in addresses:
            if street > 0:
                for j in range(40):
                    cnts[j] += street_cnts[street][j]
                    cnt_sum += cnts[j]

        if (cnt_sum == 0):
            cnt_sum = 0.1

        for j in range(40):
            target.write(',' + str((1.0 * cnts[j] + 0.1) / (cnt_sum + 40 * 0.1)))
        target.write(',' + str(int(cnt_sum)) + '\n')

    if line_cnt % 50000 == 0:
        print line_cnt

    line_cnt += 1


