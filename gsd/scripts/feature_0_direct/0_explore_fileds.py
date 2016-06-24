# coding:utf-8
# 对于全体训练集和测试集，各个字段的取值进行统计
import re
# sfcc文件夹所在的相对路径
root_dir = '../..'
basic_field_stats = file(root_dir + '/stats/0_basic_field_stats.txt', 'w')
file_names = [root_dir + '/../data/train.csv', root_dir + '/../data/test.csv']
index_map = {file_names[0] : {'Dates' : 0, 'Category' : 1, 'DayOfWeek' : 3, \
             'PdDistrict' : 4}, \
             file_names[1] : {'Dates' : 1, 'DayOfWeek' : 2, 'PdDistrict' : 3}}

for file_name in file_names:
    dataset = file(file_name)
    year_map = {}
    month_map = {}
    hour_map = {}
    dayofweek_map = {}
    pdDistrict_map = {}
    category_map = {}

    basic_field_stats.write(file_name + '\n')

    count = 0
    for line in dataset:
        # 首先，把""包括的复杂的描述项删除
        line = re.subn(r'\".*?\"', '', line)[0]

        line = line.split(',')
        if (line[0] == 'Dates' or line[0] == 'Id'):
            continue
        
        date_time = line[index_map[file_name]['Dates']].split(' ')
        date = date_time[0].split('-')
        year = date[0]
        month = date[1]
        hour = (date_time[1].split(':'))[0]

        if (year_map.has_key(year)):
            year_map[year] += 1
        else:
            year_map[year] = 1
        if (month_map.has_key(month)):
            month_map[month] += 1
        else:
            month_map[month] = 1
        if (hour_map.has_key(hour)):
            hour_map[hour] += 1
        else:
            hour_map[hour] = 1

        dayofweek = line[index_map[file_name]['DayOfWeek']]
        pdDistrict = line[index_map[file_name]['PdDistrict']]
        if (dayofweek_map.has_key(dayofweek)):
            dayofweek_map[dayofweek] += 1
        else:
            dayofweek_map[dayofweek] = 1
        if (pdDistrict_map.has_key(pdDistrict)):
            pdDistrict_map[pdDistrict] += 1
        else:
            pdDistrict_map[pdDistrict] = 1

        if (index_map[file_name].has_key('Category')):
            category = line[index_map[file_name]['Category']]
            if (category_map.has_key(category)):
                category_map[category] += 1
            else:
                category_map[category] = 1

        count += 1
        if (count % 50000 == 0):
            print count

    basic_field_stats.write('Years Distribution: \n')
    year_map = sorted(year_map.iteritems(), key=lambda d:d[0]) 
    for item in year_map:
        basic_field_stats.write(item[0] + ': ' + str(item[1]) + '\n')

    basic_field_stats.write('Months Distribution: \n')
    month_map = sorted(month_map.iteritems(), key=lambda d:d[0])
    for item in month_map:
        basic_field_stats.write(item[0] + ': ' + str(item[1]) + '\n')

    basic_field_stats.write('Hour Map: \n')
    hour_map = sorted(hour_map.iteritems(), key=lambda d:d[0])
    for item in hour_map:
        basic_field_stats.write(item[0] + ': ' + str(item[1]) + '\n')

    basic_field_stats.write('DayOfWeek Map: \n')
    days_in_a_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for week_day in days_in_a_week:
        basic_field_stats.write(week_day + ': ' + str(dayofweek_map[week_day]) + '\n')

    basic_field_stats.write('PdDistrict Map: \n')
    pdDistrict_map = sorted(pdDistrict_map.iteritems(), key=lambda d:d[0])
    for item in pdDistrict_map:
        basic_field_stats.write(item[0] + ': ' + str(item[1]) + '\n')

    if (len(category_map) != 0):
        basic_field_stats.write('Category map: \n')
        categories = 'ARSON,ASSAULT,BAD CHECKS,BRIBERY,BURGLARY,DISORDERLY CONDUCT,DRIVING UNDER THE INFLUENCE,DRUG/NARCOTIC,DRUNKENNESS,EMBEZZLEMENT,EXTORTION,FAMILY OFFENSES,FORGERY/COUNTERFEITING,FRAUD,GAMBLING,KIDNAPPING,LARCENY/THEFT,LIQUOR LAWS,LOITERING,MISSING PERSON,NON-CRIMINAL,OTHER OFFENSES,PORNOGRAPHY/OBSCENE MAT,PROSTITUTION,RECOVERED VEHICLE,ROBBERY,RUNAWAY,SECONDARY CODES,SEX OFFENSES FORCIBLE,SEX OFFENSES NON FORCIBLE,STOLEN PROPERTY,SUICIDE,SUSPICIOUS OCC,TREA,TRESPASS,VANDALISM,VEHICLE THEFT,WARRANTS,WEAPON LAWS'.split(',')
        for crime in categories:
            basic_field_stats.write(crime + ': ' + str(category_map[crime]) + '\n')










