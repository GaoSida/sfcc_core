__author__ = 'Nyunyunyunyu'
import numpy as np
import pandas as pd

train_set = pd.read_csv('../../features/0_direct/train.csv')
result = np.zeros((len(train_set),1))
result[:,0] = np.array(train_set['Category'])
all_map = {}
for col in train_set.columns:
    if col != 'Category' and col != 'Id':
        if train_set[col].dtype != 'float64':
            tmp = np.array(train_set[col])
            uni_tmp = np.unique(tmp)
            if(len(uni_tmp) > 200):
                continue
            tmp_map = {}
            for i in range(0, len(uni_tmp)):
                tmp_map[uni_tmp[i]] = i
            all_map[col] = tmp_map
            to_append = np.zeros((len(train_set), len(uni_tmp)), dtype='int64')
            for i in range(0, len(train_set)):
                to_append[i][tmp_map[tmp[i]]] = 1
            result = np.hstack((result, to_append))

pd.DataFrame(result).to_csv('train.csv', index=False)

test_set = pd.read_csv('../../features/0_direct/test.csv')
result = np.zeros((len(test_set),0))
for col in test_set.columns:
    if col != 'Category' and col != 'Id':
        if test_set[col].dtype != 'float64' and all_map.has_key(col):
            tmp_map = all_map[col]
            to_append = np.zeros((len(test_set), len(tmp_map)), dtype='int64')
            for i in range(0, len(train_set)):
                if tmp_map.has_key(tmp[i]):
                    to_append[i][tmp_map[tmp[i]]] = 1
            result = np.hstack((result, to_append))

pd.DataFrame(result).to_csv('test.csv')