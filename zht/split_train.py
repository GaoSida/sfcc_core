# coding:utf-8
# 把测试集文件一分为二

feature_dir = '../features/1_vector/'
train = file(feature_dir + 'train.csv')
fold_0 = file(feature_dir + 'fold_0.csv', 'w')
fold_1 = file(feature_dir + 'fold_1.csv', 'w')

current_fold = False
last_day_of_week = '0'
count = 0
for line in train:
    if (line[0] == 'C'):
        fold_0.write(line)
        fold_1.write(line)
        continue
    
    day_of_week = line.split(',')[94]
    if (day_of_week == '1' and last_day_of_week == '0'):
        current_fold = not current_fold
    last_day_of_week = day_of_week

    if current_fold:
        fold_1.write(line)
    else:
        fold_0.write(line)

    count += 1
    if (count % 50000 == 0):
        print count













