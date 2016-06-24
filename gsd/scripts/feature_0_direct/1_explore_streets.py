# coding:utf-8
# 探索地址、街道
import pandas as pd

# sfcc文件夹所在的相对路径
root_dir = '../..'
street_stats = file(root_dir + '/stats/1_street_stats.txt', 'w')
file_names = [root_dir + '/../data/train.csv', root_dir + '/../data/test.csv']

for file_name in file_names:
    street_stats.write(file_name + '\n')

    addresses = pd.read_csv(file_name)['Address'].values

    tot_intersection = 0
    tot_block = 0
    tot_street = 0
    street_map = {}    # 字典，街道名-提到的次数
    block_map = {}     # 二级字典，第一级是街道名，第二级是街区号，值是出现次数
    for address in addresses:
        # 统计地址形式
        intersection = address.count(' / ')
        block = address.count(' Block of ')
        tot_intersection += intersection
        tot_block += block

        if (intersection + block != 1):
            tot_street += 1

        # 根据三种形式分别处理
        if (intersection == 1):
            streets = address.split(' / ')
            for street in streets:
                if (street_map.has_key(street)):
                    street_map[street] += 1
                else:
                    street_map[street] = 1

                # 探索street的形式
                # 有三、四个词的。除了AV, ST, BL, WY。有一些特殊路名
                # 'MARTIN LUTHER KING JR DR'; 'AVENUE OF THE PALMS'
                # street = street.split()
                # if (len(street) > 2):
                #    print street
        elif (block == 1):
            block_addr = address.split(' Block of ')
            block_num = int(block_addr[0])
            if (block_map.has_key(block_addr[1])):
                if (block_map[block_addr[1]].has_key(block_num)):
                    block_map[block_addr[1]][block_num] += 1
                else:
                    block_map[block_addr[1]][block_num] = 1
            else:
                block_map[block_addr[1]] = {}
                block_map[block_addr[1]][block_num] = 1
            if (street_map.has_key(block_addr[1])):
                street_map[block_addr[1]] += 1
            else:
                street_map[block_addr[1]] = 1
        else:
            single_street = address[:-2]
            if (street_map.has_key(single_street)):
                street_map[single_street] += 1
            else:
                street_map[single_street] = 1

    street_stats.write(str(tot_intersection) + ' intersection entries\n')
    street_stats.write(str(tot_block) + ' block entries\n')
    street_stats.write(str(tot_street) + ' single street entries\n')

    print len(street_map)
    print len(block_map)
    # 一共有2000多条街道，几乎所有都被按照街区表达过












