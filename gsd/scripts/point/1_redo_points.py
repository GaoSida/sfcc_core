# coding:utf-8
# 重新计算KNN的结果，排除自己的点

from sklearn.neighbors import NearestNeighbors
import pandas as pd
import numpy as np

train_set = pd.read_csv('../../../features/0_direct/train.csv')
test_set = pd.read_csv('../../../features/0_direct/test.csv')

train_points = train_set[['Month', 'Hour', 'X', 'Y']].values
test_points = test_set[['Month', 'Hour', 'X', 'Y']].values
categories = train_set['Category'].values

nbrs = NearestNeighbors(n_neighbors=501, algorithm='ball_tree').fit(train_points)

distances, indices = nbrs.kneighbors(train_points[0:5])
for i in range(len(indices)):
    scores = np.zeros(39)
    for j in range(1, 501):
        d = distances[i][j]
        if d == 0:
            d = 0.001
        scores[categories[indices[i][j]]] += 1.0 / distances[i][j] 

    print categories[i]
    print scores























