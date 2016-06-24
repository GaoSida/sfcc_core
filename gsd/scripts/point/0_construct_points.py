# coding:utf-8
# 把KNN的结果作为输入

import math

original = file('../../../features/3_refine_street/train.csv')
knn = file('../../../features/4_points/knn_train.csv')
target = file('../../../features/4_points/train.csv', 'w')

knn.readline()

line_cnt = 0
for line in original:
    target.write(line[:-1])

    if line[0] == 'C':
    #if line[0] == 'I':
        for i in range(39):
            target.write(',point_' + str(i))
        target.write('\n')
    else:
        knn_line = knn.readline().split(',')
        for i in range(39):
            p = float(knn_line[i + 1]) + 0.0001
            target.write(',' + str(math.log(p / (1 - p))))
        target.write('\n')

    if line_cnt % 50000 == 0:
        print line_cnt

    line_cnt += 1

