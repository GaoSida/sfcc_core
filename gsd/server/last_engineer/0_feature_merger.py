# coding:utf-8
# 把新增的特征加到已有文件上面

import pandas as pd

file_key = 'fold_1'

file_name_list = ['../0_direct/' + file_key + '.csv', '../features/street_redo_' + file_key + '.csv']

df_list = []

for name in file_name_list:
    df_list.append(pd.read_csv(name))
    print "shape " + str(df_list[-1].shape)

print "start merging " + str(len(df_list))

df_full = pd.concat(df_list, axis=1)

df_full.to_csv('../features/redo_' + file_key + '_pool.csv', index=False)






