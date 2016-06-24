对数据的分析

1.时间相关性的分析

用一段时间关于各种犯罪条目的词袋来表示这段时间的特征。

两个词袋之间的相关性用相关系数衡量。

结果文件
day_corr.xls            Sheet1: 所有x日的数据汇总成一个词袋计算的相关系数矩阵

month_corr.xls          Sheet1: 将所有x月的数据汇总成一个词袋计算的相关系数矩阵
                        Sheet3: 将i月和j月对于每年分别汇总成词袋，分别计算相关系数的相关系数矩阵
                                for month_i in Months
                                for month_j in Months
                                    for year_i in Years
                                    for year_j in Years
                                        Ans(month_i, month_j) += corr(Bag(year_i, month_i), Bag(year_j, month_j))
year_corr.xls           Sheet1: 将x年的数据汇总成一个词袋计算的相关系数矩阵
week_corr.xls           Sheet1: 将所有周i的数据汇总成一个词袋计算的相关系数矩阵
                        Sheet2: 将周i和周j对于每年分别汇总成词袋，分别计算相关系数的相关系数矩阵

weekday_corr.jpg        week_corr.xls sheet1
weekday_self_corr.jpg   week_corr.xls sheet2
year_corr.jpg           year_corr.xls sheet1
month_corr.jpg          month_corr.xls sheet1
month_self_corr.jpg     month_corr.xls sheet2
day_corr.jpg            day_corr.xls sheet1

对结果的分析
基本上是时间上越接近，相关系数越大
值得注意的是2003~2005和2006~2015分布区别较大
相同的月份分布并不甚相近
星期上分布具有一致性
星期上周五~周日分布较为接近，周三周四较接近，周一较为特别，周二跟周五~周日比较接近