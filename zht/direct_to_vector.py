# coding:utf-8
# 直接把文字转义为向量
# 目前的版本暂时忽略了街道

import pickle
import re

data_dir = '../data/'
feature_dir = '../features/1_vector/'

encoder = pickle.load(file(data_dir + 'encoder.pickle'))

train_filenames = ['train.csv']
test_filenames = ['test.csv']

for filename in train_filenames:
    dataset = file(data_dir + filename)
    feature = file(feature_dir + filename, 'w')
    feature.write('Category,Y03,Y04,Y05,Y06,Y07,Y08,Y09,Y10,Y11,Y12,Y13,Y14,Y15,M1,M2,M3,M4,M5,M6,M7,M8,M9,M10,M11,M12,D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12,D13,D14,D15,D16,D17,D18,D19,D20,D21,D22,D23,D24,D25,D26,D27,D28,D29,D30,D31,H0,H1,H2,H3,H4,H5,H6,H7,H8,H9,H10,H11,H12,H13,H14,H15,H16,H17,H18,H19,H20,H21,H22,H23,Year,Month,Day,Hour,Minute,Second,DayofWeek,W1,W2,W3,W4,W5,W6,W7,PdDistrict,Pd1,Pd2,Pd3,Pd4,Pd5,Pd6,Pd7,Pd8,Pd9,Pd10,Address1,Address2,X,Y\n')
    count = 0
    for line in dataset:
        # 首先，把""包括的复杂的描述项删除
        line = re.subn(r'\".*?\"', '', line)[0]
    
        line = line.split(',')
        if (line[0] == 'Dates'):
            continue

        feature.write(str(encoder['Category'][line[1]]) + ',')
        
        #date_time = line[0].replace(' ', ',')
        #date_time = date_time.replace('-', ',')
        #date_time = date_time.replace(':', ',')
        #feature.write(date_time + ',')
        date = line[0].split(' ')
        date_day = date[0].split('-')
        date_time = date[1].split(':')
        feature.write(encoder['Year'][date_day[0]] + ',')
        feature.write(encoder['Month'][date_day[1]] + ',')
        feature.write(encoder['Day'][date_day[2]] + ',')
        feature.write(encoder['Hour'][date_time[0]] + ',')

        date_day = date[0];
        date_day = date_day.replace('-', ',')
        feature.write(date_day + ',')
        date_time = date[1];
        date_time = date_time.replace(':', ',')
        feature.write(date_time + ',')

        feature.write(str(encoder['DayOfWeek_num'][line[3]]) + ',')
        feature.write(encoder['DayOfWeek_vec'][line[3]] + ',')
        feature.write(str(encoder['PdDistrict_num'][line[4]]) + ',')
        feature.write(encoder['PdDistrict_vec'][line[4]] + ',')
        
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
    feature.write('Id,Y03,Y04,Y05,Y06,Y07,Y08,Y09,Y10,Y11,Y12,Y13,Y14,Y15,M1,M2,M3,M4,M5,M6,M7,M8,M9,M10,M11,M12,D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12,D13,D14,D15,D16,D17,D18,D19,D20,D21,D22,D23,D24,D25,D26,D27,D28,D29,D30,D31,H0,H1,H2,H3,H4,H5,H6,H7,H8,H9,H10,H11,H12,H13,H14,H15,H16,H17,H18,H19,H20,H21,H22,H23,Year,Month,Day,Hour,Minute,Second,DayofWeek,W1,W2,W3,W4,W5,W6,W7,PdDistrict,Pd1,Pd2,Pd3,Pd4,Pd5,Pd6,Pd7,Pd8,Pd9,Pd10,Address1,Address2,X,Y\n')
    count = 0

    #0,2015-05-10 23:59:00,Sunday,BAYVIEW,2000 Block of THOMAS AV,-122.39958770418998,37.7350510103906

    for line in dataset:
        line = line.split(',')
        if (line[0] == 'Id'):
            continue

        feature.write(line[0] + ',')
        
        #date_time = line[1].replace(' ', ',')
        #date_time = date_time.replace('-', ',')
        #date_time = date_time.replace(':', ',')
        #feature.write(date_time + ',')
        date = line[1].split(' ')
        date_day = date[0].split('-')
        date_time = date[1].split(':')
        feature.write(encoder['Year'][date_day[0]] + ',')
        feature.write(encoder['Month'][date_day[1]] + ',')
        feature.write(encoder['Day'][date_day[2]] + ',')
        feature.write(encoder['Hour'][date_time[0]] + ',')

        date_day = date[0];
        date_day = date_day.replace('-', ',')
        feature.write(date_day + ',')
        date_time = date[1];
        date_time = date_time.replace(':', ',')
        feature.write(date_time + ',')

        feature.write(str(encoder['DayOfWeek_num'][line[2]]) + ',')
        feature.write(encoder['DayOfWeek_vec'][line[2]] + ',')
        feature.write(str(encoder['PdDistrict_num'][line[3]]) + ',')
        feature.write(encoder['PdDistrict_vec'][line[3]] + ',')
        
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









