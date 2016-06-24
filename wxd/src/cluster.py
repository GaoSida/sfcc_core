# coding=utf-8
__author__ = 'Nyunyunyunyu'

from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math

data = pd.read_csv('../../features/0_direct/train.csv')
data = data.loc[:, ['Category', 'X', 'Y']]
data = data[data.Y < 40]
data_grouped = data.groupby(data.Category)


color = np.array(['b', 'g', 'r', 'c', 'm', 'y'])

points = np.array(data.loc[:, ['X', 'Y']])
dis = []
columns_name = []
for cat_data in data_grouped:
    tmp = cat_data[1].loc[:, ['X', 'Y']]
    if len(tmp) < 100:
        continue
    print "For %d: " % cat_data[0]
    columns_name.append("To%d" %cat_data[0])
    group = tmp.groupby(lambda x:random.randint(0,1))
    train_data = group.get_group(0)
    test_data = group.get_group(1)
    score = float('inf')
    K = 0
    for i in range(1, 8):
        oracle = KMeans(init='k-means++', n_clusters=i, n_init=10)
        oracle.fit(train_data)
        score_val = oracle.score(test_data)
        score_val = math.fabs(math.fabs(score_val) - oracle.inertia_) / oracle.inertia_
        if score_val < score:
            score = score_val
            K = i
    best = KMeans(init='k-means++', n_clusters=K, n_init=10)
    best.fit(tmp)
    label = best.predict(points)
    belong_point = best.cluster_centers_[label]
    dis.append(np.power(np.sum(np.power(belong_point - points,2), axis=1), 0.5))
pd.DataFrame(np.column_stack(dis), columns=columns_name).to_csv('vec.csv', index=False)

