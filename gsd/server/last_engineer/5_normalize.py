# coding:utf-8
# 对数据点进行标准化

import pandas as pd
import numpy as np

train = pd.read_csv('/Users/gaosida/desktop/sfcc/features/0_direct/train.csv')
test = pd.read_csv('/Users/gaosida/desktop/sfcc/features/0_direct/test.csv')

train['Month'] = (train['Month'] - np.mean(train['Month'])) / np.std(train['Month'])
train['Hour'] = (train['Hour'] - np.mean(train['Hour'])) / np.std(train['Hour'])
train['X'] = (train['X'] - np.mean(train['X'])) / np.std(train['X'])
train['Y'] = (train['Y'] - np.mean(train['Y'])) / np.std(train['Y'])

test['Month'] = (test['Month'] - np.mean(test['Month'])) / np.std(test['Month'])
test['Hour'] = (test['Hour'] - np.mean(test['Hour'])) / np.std(test['Hour'])
test['X'] = (test['X'] - np.mean(test['X'])) / np.std(test['X'])
test['Y'] = (test['Y'] - np.mean(test['Y'])) / np.std(test['Y'])

train.to_csv('/Users/gaosida/desktop/sfcc/features/0_direct/train_norm.csv', index=False)
train.to_csv('/Users/gaosida/desktop/sfcc/features/0_direct/test_norm.csv', index=False)





