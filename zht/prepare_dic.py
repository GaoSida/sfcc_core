# coding:utf-8
# 准备编码用的字典

import pickle
import pandas as pd

data_dir = '../data/'

encoder = {}

pd2num = {'BAYVIEW' : 1, 'CENTRAL' : 2, 'INGLESIDE' : 3, 'MISSION' : 4, 'NORTHERN' : 5, 'PARK' : 6, 'RICHMOND' : 7, 'SOUTHERN' : 8, 'TARAVAL' : 9, 'TENDERLOIN' : 10}
encoder['PdDistrict_num'] = pd2num

pd2vec = {'BAYVIEW' : '1,0,0,0,0,0,0,0,0,0', 'CENTRAL' : '0,1,0,0,0,0,0,0,0,0', 'INGLESIDE' : '0,0,1,0,0,0,0,0,0,0', 'MISSION' : '0,0,0,1,0,0,0,0,0,0', 'NORTHERN' : '0,0,0,0,1,0,0,0,0,0', 'PARK' : '0,0,0,0,0,1,0,0,0,0', 'RICHMOND' : '0,0,0,0,0,0,1,0,0,0', 'SOUTHERN' : '0,0,0,0,0,0,0,1,0,0', 'TARAVAL' : '0,0,0,0,0,0,0,0,1,0', 'TENDERLOIN' : '0,0,0,0,0,0,0,0,0,1'}
encoder['PdDistrict_vec'] = pd2vec

def make_dic(num, start):
    dic = {}
    for n in range(0, num):
        vec = ''
        for m in range(0, num):
            if m < n:
                vec = vec + '0'
            elif m == n:
                vec = vec + '1'
            else:
                vec = vec + '0'
            if m != num-1:
                vec = vec + ','
        key = str(start+n)
        if start + n < 10:
            key = '0' + key
        dic[key] = vec
    return dic

dayofWeek2num = {'Monday' : 1, 'Tuesday' : 2, 'Wednesday' : 3, 'Thursday' : 4, \
           'Friday' : 5, 'Saturday' : 6, 'Sunday' : 7}
encoder['DayOfWeek_num'] = dayofWeek2num

dayofWeek2vec = {'Monday' : '1,0,0,0,0,0,0', 'Tuesday' : '0,1,0,0,0,0,0', 'Wednesday' : '0,0,1,0,0,0,0', 'Thursday' : '0,0,0,1,0,0,0', 'Friday' : '0,0,0,0,1,0,0', 'Saturday' : '0,0,0,0,0,1,0', 'Sunday' : '0,0,0,0,0,0,1'}
encoder['DayOfWeek_vec'] = dayofWeek2vec

year2vec = make_dic(13, 2003)
encoder['Year'] = year2vec 

month2vec = make_dic(12, 1)
encoder['Month'] = month2vec

day2vec = make_dic(31, 1)
encoder['Day'] = day2vec

hour2vec = make_dic(24, 0)
encoder['Hour'] = hour2vec


crimes = 'ARSON,ASSAULT,BAD CHECKS,BRIBERY,BURGLARY,DISORDERLY CONDUCT,DRIVING UNDER THE INFLUENCE,DRUG/NARCOTIC,DRUNKENNESS,EMBEZZLEMENT,EXTORTION,FAMILY OFFENSES,FORGERY/COUNTERFEITING,FRAUD,GAMBLING,KIDNAPPING,LARCENY/THEFT,LIQUOR LAWS,LOITERING,MISSING PERSON,NON-CRIMINAL,OTHER OFFENSES,PORNOGRAPHY/OBSCENE MAT,PROSTITUTION,RECOVERED VEHICLE,ROBBERY,RUNAWAY,SECONDARY CODES,SEX OFFENSES FORCIBLE,SEX OFFENSES NON FORCIBLE,STOLEN PROPERTY,SUICIDE,SUSPICIOUS OCC,TREA,TRESPASS,VANDALISM,VEHICLE THEFT,WARRANTS,WEAPON LAWS'.split(',')
crime2num = {}
for i in range(len(crimes)):
    crime2num[crimes[i]] = i
encoder['Category'] = crime2num

file_names = [data_dir + 'train.csv', data_dir + 'test.csv']
street_list = {}
for file_name in file_names:
    addresses = pd.read_csv(file_name)['Address'].values
    for address in addresses:
        intersection = address.count(' / ')
        block = address.count(' Block of ')
        if (intersection == 1):
            streets = address.split(' / ')
            for street in streets:
                if (street[0] == ' '):
                    street = street[1:]
                street_list[street] = 1
        elif (block == 1):
            block_addr = address.split(' Block of ')
            if (block_addr[1][0] == ' '):
                block_addr[1] = block_addr[1][1:]
            street_list[block_addr[1]] = 1
        else:
            single_street = address[:-2]
            if (single_street[0] == ' '):
                single_street = single_street[1:]
            street_list[single_street] = 1
street_list = sorted(street_list.iteritems(), key=lambda d:d[0])
print len(street_list)
street2num = {}
#street_name_list = file('../../stats/2_street_list.txt', 'w')
for i in range(len(street_list)):
    street2num[street_list[i][0]] = i + 1
#    street_name_list.write(street_list[i][0] + '\n')

encoder['Street'] = street2num

decoder = {'DayOfWeek_num' : {}, 'DayOfWeek_vec' : {}, 'PdDistrict_num' : {}, 'PdDistrict_vec' : {}, 'Category' : {}, 'Street' : {}, 'Year' : {}, 'Month' : {}, 'Day' : {}, 'Hour' : {}}
for key in dayofWeek2vec.keys():
    decoder['DayOfWeek_vec'][dayofWeek2vec[key]] = key
for key in dayofWeek2num.keys():
    decoder['DayOfWeek_num'][dayofWeek2num[key]] = key
for key in pd2vec.keys():
    decoder['PdDistrict_vec'][pd2vec[key]] = key
for key in pd2num.keys():
    decoder['PdDistrict_num'][pd2num[key]] = key
for key in crime2num.keys():
    decoder['Category'][crime2num[key]] = key
for key in street2num.keys():
    decoder['Street'][street2num[key]] = key
for key in year2vec.keys():
    decoder['Year'][year2vec[key]] = key
for key in month2vec.keys():
    decoder['Month'][month2vec[key]] = key
for key in day2vec.keys():
    decoder['Day'][day2vec[key]] = key
for key in hour2vec.keys():
    decoder['Hour'][hour2vec[key]] = key

encoder_file = file(data_dir + 'encoder.pickle', 'w')
decoder_file = file(data_dir + 'decoder.pickle', 'w')
pickle.dump(encoder, encoder_file)
pickle.dump(decoder, decoder_file)



