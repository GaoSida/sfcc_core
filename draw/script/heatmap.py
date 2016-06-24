# coding:utf-8
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
# crimeData.head()

crimeData['Dates'] = pd.to_datetime(crimeData["Dates"])
crimeData['Year'] = crimeData['Dates'].dt.year
crimeData['Month'] = crimeData['Dates'].dt.month
crimeData['Hour'] = crimeData['Dates'].dt.hour
month_map = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
             7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
crimeData['Month'].replace(month_map, inplace=True)
crimeData['Year'] = crimeData['Year'].astype(str)
crimeData['Hour'] = crimeData['Hour'].astype(str)
# crimeData.head()

YearlyData = pd.DataFrame(crimeData["Year"].value_counts())
MonthlyData = pd.DataFrame(crimeData["Month"].value_counts())
# WeeklyData = pd.DataFrame(crimeData["DayOfWeek"].value_counts(sort=False))
HourlyData = pd.DataFrame(crimeData["Hour"].value_counts())
DistrictData = pd.DataFrame(crimeData["PdDistrict"].value_counts())


DayOfWeek = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']
Hour = [0, 1, 10, 11, 12, 13, 14, 15, 16, 17,
        18, 19, 20, 21, 22, 23, 3, 4, 5, 6, 7, 8, 9]
CategoryGroup = crimeData.groupby('Category')


# 对ASSAULT绘制hour-dayofweek的heatmap，现在的问题是hour没法按照顺序排序
CrimeGroup = CategoryGroup.get_group('ASSAULT')
counts = []
WeeklyGroup = CrimeGroup.groupby('DayOfWeek')
for day in DayOfWeek:
    DayGroup = WeeklyGroup.get_group(day)
    daycounts = DayGroup['Hour'].value_counts(sort=False)
    counts.append(pd.Series.sort_index(daycounts))

countsMatrix = counts[0]
for i in range(1, 7):
    countsMatrix = np.column_stack((countsMatrix, counts[i]))

print countsMatrix

fig, ax = plt.subplots()
heatmap = ax.pcolor(countsMatrix, cmap=plt.cm.Blues)
#ax.set_xticks(np.arange(countsMatrix.shape[0]) + 2, minor=False)
#ax.set_yticks(np.arange(countsMatrix.shape[1]) + 2, minor=False)
ax.set_xticklabels(DayOfWeek, minor=False)
ax.set_yticklabels(Hour, minor=False)
plt.show()
