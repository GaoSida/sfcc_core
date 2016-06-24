import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
import pdb
from math import log
import math
class JSD:
    def KLD(self,p,q):
        if 0 in q :
            raise ValueError
        return sum(_p * log(_p/_q) for (_p,_q) in zip(p,q) if _p!=0)

    def JSD_core(self,p,q):
        _p = p / np.linalg.norm(p)
        _q = q / np.linalg.norm(q)
        M = 0.5*(_p + _q)
        return 0.5*self.KLD(_p,M)+0.5*self.KLD(_q,M)

jsd = JSD()

train_set = pd.read_csv('../../data/train.csv')
train_set.Dates = pd.to_datetime(train_set.Dates)

weekday_set = train_set.loc[:, ['DayOfWeek', 'Dates', 'Category']]
weekday_set.set_index('Dates')

weekday_grouped = weekday_set.groupby(weekday_set.DayOfWeek)
weekday_corr = {}
weekday_corr_matrix = []
weekday_every_year_matrix = []
for weeki in weekday_grouped:
    icounts = weeki[1].Category.value_counts()
    row_corr = {}
    weekday_corr_row = []
    year_week_i = weeki[1].set_index('Dates').groupby(lambda x: x.year)
    weekday_every_year_row = []
    for weekj in weekday_grouped:
        jcounts = weekj[1].Category.value_counts()
        row_corr[weekj[0]] = log(jsd.JSD_core(np.array(icounts), np.array(jcounts))+1)
        weekday_corr_row.append(row_corr[weekj[0]])
        year_week_j = weekj[1].set_index('Dates').groupby(lambda x: x.year)
        tmp_sum = 0
        tmp_cnt = 0
        for bin_i in year_week_i:
            for bin_j in year_week_j:
                tmp_sum += log(1+jsd.JSD_core(np.array(bin_i[1].Category.value_counts()), np.array(bin_j[1].Category.value_counts())))
                tmp_cnt += 1
        tmp_sum /= tmp_cnt
        weekday_every_year_row.append(tmp_sum)
    weekday_every_year_matrix.append(weekday_every_year_row)
    weekday_corr[weeki[0]] = row_corr
    weekday_corr_matrix.append(weekday_corr_row)

writer = pd.ExcelWriter('../analyse/weekday_corr.xls')
pd.DataFrame(weekday_corr).to_excel(writer, 'Sheet1')
pd.DataFrame(weekday_every_year_matrix).to_excel(writer, 'Sheet2')
writer.close()

fig_week_year = plt.figure()
weekday_every_year_matrix = np.matrix(weekday_every_year_matrix)
week_year_plot = fig_week_year.add_subplot(1,1,1)
week_year_plot.set_aspect('equal')
week_year_plot.set_title('every year weekday-weekday')
plt.imshow(weekday_every_year_matrix , interpolation='nearest', cmap=plt.cm.ocean, extent=(0.5,np.shape(weekday_every_year_matrix)[0]+0.5,0.5,np.shape(weekday_every_year_matrix)[1]+0.5))
plt.colorbar()
savefig('../analyse/weekday_self_corr.jpg')

fig_week = plt.figure()
week_corr_matrix = np.matrix(weekday_corr_matrix)
week_plot = fig_week.add_subplot(1,1,1)
week_plot.set_aspect('equal')
week_plot.set_title('weekday-weekday')
plt.imshow(weekday_corr_matrix , interpolation='nearest', cmap=plt.cm.ocean, extent=(0.5,np.shape(week_corr_matrix)[0]+0.5,0.5,np.shape(week_corr_matrix)[1]+0.5))
plt.colorbar()
savefig('../analyse/weekday_corr.jpg')

train_set = train_set.loc[:, ['Dates', 'Category']]
train_set = train_set.set_index('Dates')

year_label = []
year_corr_matrix = []
year_grouped = train_set.groupby(lambda x: x.year)
year_corr = {}
for yeari in year_grouped:
    icounts = yeari[1].Category.value_counts()
    row_corr = {}
    year_corr_row = []
    for yearj in year_grouped:
        jcounts = yearj[1].Category.value_counts()
        row_corr[yearj[0]] = log(1+jsd.JSD_core(np.array(icounts), np.array(jcounts)))
        year_corr_row.append(row_corr[yearj[0]])
    year_corr_matrix.append(year_corr_row)
    year_corr[yeari[0]] = row_corr
pd.DataFrame(year_corr).to_excel('../analyse/year_corr.xls')

fig_year = plt.figure()
year_corr_matrix = np.matrix(year_corr_matrix)
year_plot = fig_year.add_subplot(1,1,1)
year_plot.set_aspect('equal')
year_plot.set_title('year-year')
plt.imshow(year_corr_matrix , interpolation='nearest', cmap=plt.cm.ocean, extent=(0.5,np.shape(year_corr_matrix)[0]+0.5,0.5,np.shape(year_corr_matrix)[1]+0.5))
plt.colorbar()
savefig('../analyse/year_corr.jpg')

month_grouped = train_set.groupby(lambda x: x.month)
month_corr = {}
month_most_realted = {}
month_label = []
month_corr_matrix = []
month_every_year = []
for monthi in month_grouped:
    icounts = monthi[1].Category.value_counts()
    row_corr = {}
    most = -1
    corr_val = 0
    month_corr_row = []
    month_label.append(monthi[0])
    year_month_i = monthi[1].groupby(lambda x: x.year)
    month_every_year_row = []
    for monthj in month_grouped:
        jcounts = monthj[1].Category.value_counts()
        row_corr[monthj[0]] = log(1+jsd.JSD_core(np.array(icounts), np.array(jcounts)))
        month_corr_row.append(row_corr[monthj[0]])
        if monthj[0] != monthi[0] and abs(row_corr[monthj[0]]) > corr_val:
            most = monthj[0]
            corr_val = row_corr[monthj[0]]
        year_month_j = monthj[1].groupby(lambda x: x.year)
        tmp_sum = 0
        tmp_cnt = 0
        for bin_i in year_month_i:
            for bin_j in year_month_j:
                tmp_sum += log(1+jsd.JSD_core(np.array(bin_i[1].Category.value_counts()), np.array(bin_j[1].Category.value_counts())))
                tmp_cnt += 1
        tmp_sum /= tmp_cnt
        month_every_year_row.append(tmp_sum)
    month_every_year.append(month_every_year_row)
    month_corr_matrix.append(month_corr_row)
    month_corr[monthi[0]] = row_corr
    month_most_realted[monthi[0]] = {'month': most, 'corr': corr_val}

fig_month = plt.figure()
month_corr_matrix = np.matrix(month_corr_matrix)
month_plot = fig_month.add_subplot(1,1,1)
month_plot.set_aspect('equal')
month_plot.set_title('month-month')
plt.imshow(month_corr_matrix , interpolation='nearest', cmap=plt.cm.ocean, extent=(0.5,np.shape(month_corr_matrix)[0]+0.5,0.5,np.shape(month_corr_matrix)[1]+0.5))
plt.colorbar()
savefig('../analyse/month_corr.jpg')

fig_month_year = plt.figure()
month_year_matrix = np.matrix(month_every_year)
month_year_plot = fig_month_year.add_subplot(1,1,1)
month_year_plot.set_aspect('equal')
month_year_plot.set_title('every year month-month')
plt.imshow(month_year_matrix , interpolation='nearest', cmap=plt.cm.ocean, extent=(0.5,np.shape(month_year_matrix)[0]+0.5,0.5,np.shape(month_year_matrix)[1]+0.5))
plt.colorbar()
savefig('../analyse/month_self_corr.jpg')

writer = pd.ExcelWriter('../analyse/month_corr.xls')
pd.DataFrame(month_corr).to_excel(writer, 'Sheet1')
pd.DataFrame(month_most_realted).to_excel(writer, 'Sheet2')
pd.DataFrame(month_every_year).to_excel(writer, 'Sheet3')
writer.save()


day_corr_matrix = []
day_grouped = train_set.groupby(lambda x: x.day)
day_corr = {}
for dayi in day_grouped:
    icounts = dayi[1].Category.value_counts()
    row_corr = {}
    day_corr_row = []
    for dayj in day_grouped:
        jcounts = dayj[1].Category.value_counts()
        row_corr[dayj[0]] = log(1+jsd.JSD_core(np.array(icounts), np.array(jcounts)))
        day_corr_row.append(row_corr[dayj[0]])
    day_corr[dayi[0]] = row_corr
    day_corr_matrix.append(day_corr_row)
pd.DataFrame(day_corr).to_excel('../analyse/day_corr.xls')

fig_day = plt.figure()
day_corr_matrix = np.matrix(day_corr_matrix)
day_plot = fig_day.add_subplot(1,1,1)
day_plot.set_aspect('equal')
day_plot.set_title('day-day')
plt.imshow(day_corr_matrix , interpolation='nearest', cmap=plt.cm.ocean, extent=(0.5,np.shape(day_corr_matrix)[0]+0.5,0.5,np.shape(day_corr_matrix)[1]+0.5))
plt.colorbar()

savefig('../analyse/day_corr.jpg')