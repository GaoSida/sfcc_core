# coding:utf-8
# 把两组训练数据合并

import pandas as pd

file_name_list = ['../features/redo_fold_0_pool.csv', '../features/redo_fold_1_pool.csv']

df_list = []

for name in file_name_list:
    df_list.append(pd.read_csv(name))
    print "shape " + str(df_list[-1].shape)

print "start merging " + str(len(df_list))

df_full = pd.concat(df_list, axis=1)

df_full.to_csv('../features/redo_2folds_pool.csv', index=False)

