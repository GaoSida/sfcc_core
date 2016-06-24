# coding:utf-8
# 直接把文字转义为向量
# 目前的版本暂时忽略了街道

import pickle
import re

data_dir = '../../../data/'
feature_dir = '../../../features/0_direct/'

encoder = pickle.load(file(data_dir + 'encoder.pickle'))

train_filenames = ['train.csv']
test_filenames = ['test.csv']

for filename in train_filenames:
    dataset = file(data_dir + filename)
    feature = file(feature_dir + filename, 'w')
    feature.write('Category,Year,Month,Day,Hour,Minute,Second,DayOfWeek,PdDistrict,Address1,Address2,X,Y\n')
    count = 0
    for line in dataset:
        # 首先，把""包括的复杂的描述项删除
        line = re.subn(r'\".*?\"', '', line)[0]
    
        line = line.split(',')
        if (line[0] == 'Dates'):
            continue

        feature.write(str(encoder['Category'][line[1]]) + ',')
        
        date_time = line[0].replace(' ', ',')
        date_time = date_time.replace('-', ',')
        date_time = date_time.replace(':', ',')
        feature.write(date_time + ',')
        feature.write(str(encoder['DayOfWeek'][line[3]]) + ',')
        feature.write(str(encoder['PdDistrict'][line[4]]) + ',')
        
        # 对地址进行编码
        address = line[6]
        intersection = address.count(' / ')
        block = address.count(' Block of ')
        if (intersection == 1):
            streets = address.split(' / ')
            street_0 = encoder['Street'][streets[0]]
            street_1 = encoder['Street'][streets[1]]
            feature.write(str(min(street_0, street_1)) + ',' + str(max(street_0, street_1)) + ',')
        elif (block == 1):
            block_addr = address.split(' Block of ')
            if (block_addr[1][0] == ' '):
                block_addr[1] = block_addr[1][1:]
            feature.write(str(0 - int(block_addr[0])) + ',' + str(encoder['Street'][block_addr[1]]) + ',')
        else:
            single_street = address[:-2]
            if (single_street[0] == ' '):
                single_street = single_street[1:]
            feature.write(str(encoder['Street'][single_street]) + ',-1,')

        feature.write(line[7] + ',' + line[8])

        count += 1
        if (count % 50000 == 0):
            print count


for filename in test_filenames:
    dataset = file(data_dir + filename)
    feature = file(feature_dir + filename, 'w')
    feature.write('Id,Year,Month,Day,Hour,Minute,Second,DayOfWeek,PdDistrict,Address1,Address2,X,Y\n')
    count = 0
    for line in dataset:
        line = line.split(',')
        if (line[0] == 'Id'):
            continue

        feature.write(line[0] + ',')
        
        date_time = line[1].replace(' ', ',')
        date_time = date_time.replace('-', ',')
        date_time = date_time.replace(':', ',')
        feature.write(date_time + ',')
        feature.write(str(encoder['DayOfWeek'][line[2]]) + ',')
        feature.write(str(encoder['PdDistrict'][line[3]]) + ',')
        
        # 对地址进行编码
        address = line[4]
        intersection = address.count(' / ')
        block = address.count(' Block of ')
        if (intersection == 1):
            streets = address.split(' / ')
            street_0 = encoder['Street'][streets[0]]
            street_1 = encoder['Street'][streets[1]]
            feature.write(str(min(street_0, street_1)) + ',' + str(max(street_0, street_1)) + ',')
        elif (block == 1):
            block_addr = address.split(' Block of ')
            if (block_addr[1][0] == ' '):
                block_addr[1] = block_addr[1][1:]
            feature.write(str(0 - int(block_addr[0])) + ',' + str(encoder['Street'][block_addr[1]]) + ',')
        else:
            single_street = address[:-2]
            if (single_street[0] == ' '):
                single_street = single_street[1:]
            feature.write(str(encoder['Street'][single_street]) + ',-1,')

        feature.write(line[5] + ',' + line[6])

        count += 1
        if (count % 50000 == 0):
            print count









