# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will
# list the files in the input directory
# Any results you write to the current directory are saved as output.

import seaborn as sns
import matplotlib.pyplot as plt

crimeData = pd.read_csv('../input/train.csv')
print(crimeData.shape)

crimeData['Dates'] = pd.to_datetime(crimeData["Dates"])
crimeData['Year'] = crimeData['Dates'].dt.year
crimeData['Month'] = crimeData['Dates'].dt.month
crimeData['Hour'] = crimeData['Dates'].dt.hour
month_map = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
             7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
crimeData['Month'].replace(month_map, inplace=True)
crimeData['Year'] = crimeData['Year'].astype(str)
crimeData['Hour'] = crimeData['Hour'].astype(str)

YearlyData = pd.DataFrame(crimeData["Year"].value_counts())
MonthlyData = pd.DataFrame(crimeData["Month"].value_counts(sort=False))
WeeklyData = pd.DataFrame(crimeData["DayOfWeek"].value_counts(sort=False))
HourlyData = pd.DataFrame(crimeData["Hour"].value_counts(sort=False))
DistrictData = pd.DataFrame(crimeData["PdDistrict"].value_counts())
CategoryData = pd.DataFrame(crimeData["Category"].value_counts(sort=True))

plt.figure(figsize=(16, 10))
'''
weekday = [u'Monday', u'Tuesday', u'Wednesday', u'Thursday', u'Friday', u'Saturday', u'Sunday']
wd = []
for day in weekday:
    wd.append(WeeklyData.loc[day, 'DayOfWeek'])
wd = pd.DataFrame(wd)
wd.index = weekday
wd.columns = ['DayOfWeek']
'''
#sns.barplot(x=wd.index, y="DayOfWeek", data=wd)

# sns.barplot(x=HourlyData.index, y="Hour", data=HourlyData, order=[
#    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'])

month = [u'Jan', u'Feb', u'Mar', u'Apr', u'May', u'Jun', u'Jul', u'Aug', u'Sep',
       u'Oct', u'Nov', u'Dec']
md = []
for m in month:
    md.append(MonthlyData.loc[m, 'Month'])
md = pd.DataFrame(md)
md.index = month
md.columns = ['Month']
#sns.barplot(x=md.index, y="Month", data=md)
#print MonthlyData.index

# sns.barplot(x=YearlyData.index, y="Year", data=YearlyData)
sns.barplot(x="Category", y=CategoryData.index, data=CategoryData)

#sns.barplot(x=DistrictData.index, y="PdDistrict", data=DistrictData)

plt.savefig('test.png')
