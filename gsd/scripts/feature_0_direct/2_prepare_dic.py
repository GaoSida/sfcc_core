# coding:utf-8
# 准备编码用的字典

import pickle
import pandas as pd

data_dir = '../../../data/'

encoder = {}
day2num = {'Monday' : 1, 'Tuesday' : 2, 'Wednesday' : 3, 'Thursday' : 4, \
           'Friday' : 5, 'Saturday' : 6, 'Sunday' : 7}
encoder['DayOfWeek'] = day2num

pd2num = {'BAYVIEW' : 1, 'CENTRAL' : 2, 'INGLESIDE' : 3, 'MISSION' : 4, 'NORTHERN' : 5, \
          'PARK' : 6, 'RICHMOND' : 7, 'SOUTHERN' : 8, 'TARAVAL' : 9, 'TENDERLOIN' : 10}
encoder['PdDistrict'] = pd2num

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
street_name_list = file('../../stats/2_street_list.txt', 'w')
for i in range(len(street_list)):
    street2num[street_list[i][0]] = i + 1
    street_name_list.write(street_list[i][0] + '\n')

encoder['Street'] = street2num

decoder = {'DayOfWeek' : {}, 'PdDistrict' : {}, 'Category' : {}, 'Street' : {}}
for key in day2num.keys():
    decoder['DayOfWeek'][day2num[key]] = key
for key in pd2num.keys():
    decoder['PdDistrict'][pd2num[key]] = key
for key in crime2num.keys():
    decoder['Category'][crime2num[key]] = key
for key in street2num.keys():
    decoder['Street'][street2num[key]] = key

encoder_file = file(data_dir + 'encoder.pickle', 'w')
decoder_file = file(data_dir + 'decoder.pickle', 'w')
pickle.dump(encoder, encoder_file)
pickle.dump(decoder, decoder_file)



