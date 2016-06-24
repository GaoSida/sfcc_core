# coding:utf-8
# 在街道的基础上加上1 of k形式编码的警察局和星期几

import pickle
import math
import numpy as np
import pandas as pd


original = file('../../../features/2_street/test.csv')
target = file('../../../features/2_street_bin/test.csv', 'w')

line_cnt = 0
for line in original:
    line = line.split(',')

    #if line[0][0] == 'C':
    if line[0][0] == 'I':
        for entry in line[:-1]:
            target.write(entry + ',')
        target.write(line[-1][:-1])

        for i in range(7):
            target.write(',week_day_' + str(i + 1))
        for i in range(10):
            target.write(',pd_' + str(i + 1))
        target.write('\n')
    else:
        for entry in line[:13]:
            target.write(entry + ',')

        for entry in line[13:53]:
            #p = float(entry)
            #target.write(str(math.log(p / (1 - p))) + ',')
            target.write(entry + ',')

        #target.write(str(math.log(float(line[53]) + 1)))
        target.write(line[53][:-1])

        day_of_week = int(line[7])
        day_vector = np.zeros(7)
        day_vector[day_of_week - 1] = 1

        pd = int(line[8])
        pd_vector = np.zeros(10)
        pd_vector[pd - 1] = 1

        for i in range(7):
            target.write(',' + str(int(day_vector[i])))
        for i in range(10):
            target.write(',' + str(int(pd_vector[i])))
        target.write('\n')
    if line_cnt % 50000 == 0:
        print line_cnt

    line_cnt += 1


