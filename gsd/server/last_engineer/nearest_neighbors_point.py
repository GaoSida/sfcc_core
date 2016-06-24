# coding:utf-8
# 按照距离对每个人属于各个类的可能性进行打分

from sklearn.neighbors import NearestNeighbors
import pandas as pd
import numpy as np
import math

train_set = pd.read_csv('../0_direct/train.csv')
test_set = pd.read_csv('../0_direct/test.csv')

point_dim = 4
train_points = train_set[['Month', 'Hour', 'X', 'Y']].values
test_points = test_set[['Month', 'Hour', 'X', 'Y']].values

# 归一化，各个维度
for i in range(point_dim):
    train_points[:, i] = (train_points[:, i] - np.mean(train_points[:, i])) / np.std(train_points[:, i])
    test_points[:, i] = (test_points[:, i] - np.mean(test_points[:, i])) / np.std(test_points[:, i])

print "done normalizing"

categories = train_set['Category'].values

nbrs = NearestNeighbors(n_neighbors=3001, algorithm='ball_tree').fit(train_points)

train_target = file('../features/train_points.csv', 'w')
for i in range(39):
    train_target.write('points_' + str(i) + ',')
train_target.write('\n')

for i in range(len(train_points)):
    if (i % 1000 == 0):
        print "done train " + str(i)

    distances, indices = nbrs.kneighbors(train_points[i].reshape(-1, point_dim))
    # 计算分数
    scores = np.ones(39)      # 平滑处理
    for j in range(1, 3001):
        d = distances[0][j]
        if d < 0.001:
            d = 0.001
        scores[categories[indices[0][j]]] += 1.0 / d

    # 分数取对数
    for j in range(39):
        train_target.write(str(math.log(scores[j] + 1)) + ',')
    train_target.write('\n')

'''
test_target = file('../features/test_points.csv', 'w')
for i in range(39):
    test_target.write('points_' + str(i) + ',')
test_target.write('\n')

for i in range(len(test_points)):
    if (i % 1000 == 0):
        print "done train " + str(i)

    distances, indices = nbrs.kneighbors(test_points[i].reshape(-1, point_dim))
    # 计算分数
    scores = np.ones(39)      # 平滑处理
    for j in range(1, 3001):
        d = distances[0][j]
        if d < 0.001:
            d = 0.001
        scores[categories[indices[0][j]]] += 1.0 / d

    # 分数取对数
    for j in range(39):
        test_target.write(str(math.log(scores[j] + 1)) + ',')
    test_target.write('\n')
'''



















