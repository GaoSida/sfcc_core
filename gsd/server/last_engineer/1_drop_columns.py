# coding:utf-8
# 删除一些列

import pandas as pd
import numpy as np

file_key = 'train'
df = pd.read_csv('../features/' + file_key + '_pool.csv')
columns2drop = "points_0,points_1,points_2,points_3,points_4,points_5,points_6,points_7,points_8,points_9,points_10,points_11,points_12,points_13,points_14,points_15,points_16,points_17,points_18,points_19,points_20,points_21,points_22,points_23,points_24,points_25,points_26,points_27,points_28,points_29,points_30,points_31,points_32,points_33,points_34,points_35,points_36,points_37,points_38,Unnamed: 39,Unnamed: 39.1".split(',')

df = df.drop(columns2drop, axis = 1)

df.to_csv('../features/' + file_key + '_pool.csv')

