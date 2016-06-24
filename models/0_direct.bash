#!/bin/bash

echo 'start'
# 这一条命令对应的是目前的那次提交，log_loss=2.45524
#python baselines.py rf_direct_feature /0_direct/train.csv /0_direct/test.csv /0_direct/fold_0.csv /0_direct/fold_1.csv 'Year,Month,Day,Hour,Minute,Second,DayOfWeek,PdDistrict,Address1,Address2,X,Y' Category rf 'n_estimators:i:30 max_depth:i:8 min_samples_leaf:i:80 random_state:i:0 n_jobs:i:10 verbose:i:1' ./pred log.txt sub

# LogLoss: 2.71427084335
#python baselines.py gb_direct_feature /0_direct/train.csv /0_direct/test.csv /0_direct/fold_0.csv /0_direct/fold_1.csv 'Year,Month,Day,Hour,Minute,Second,DayOfWeek,PdDistrict,Address1,Address2,X,Y' Category gb 'n_estimators:i:10 learning_rate:f:0.1 max_depth:i:1 min_samples_leaf:i:80 random_state:i:0 verbose:i:1' ./pred log.txt cv

# LogLoss: 2.57284966218
python baselines.py gb_direct_feature /0_direct/train.csv /0_direct/test.csv /0_direct/fold_0.csv /0_direct/fold_1.csv 'Year,Month,Day,Hour,Minute,Second,DayOfWeek,PdDistrict,Address1,Address2,X,Y' Category gb 'n_estimators:i:20 learning_rate:f:0.1 max_depth:i:1 min_samples_leaf:i:80 random_state:i:0 verbose:i:1' ./pred log.txt cv

echo
echo '============================================================'
echo

# LogLoss: 3.36706059829
python baselines.py gb_direct_feature /0_direct/train.csv /0_direct/test.csv /0_direct/fold_0.csv /0_direct/fold_1.csv 'Year,Month,Day,Hour,Minute,Second,DayOfWeek,PdDistrict,Address1,Address2,X,Y' Category gb 'n_estimators:i:10 learning_rate:f:0.01 max_depth:i:1 min_samples_leaf:i:80 random_state:i:0 verbose:i:1' ./pred log.txt cv

echo
echo '============================================================'
echo

# LogLoss: 2.65828788356
python baselines.py gb_direct_feature /0_direct/train.csv /0_direct/test.csv /0_direct/fold_0.csv /0_direct/fold_1.csv 'Year,Month,Day,Hour,Minute,Second,DayOfWeek,PdDistrict,Address1,Address2,X,Y' Category gb 'n_estimators:i:10 learning_rate:f:0.1 max_depth:i:2 min_samples_leaf:i:80 random_state:i:0 verbose:i:1' ./pred log.txt cv

echo
echo '============================================================'
echo

# LogLoss: 2.71427086956
python baselines.py gb_direct_feature /0_direct/train.csv /0_direct/test.csv /0_direct/fold_0.csv /0_direct/fold_1.csv 'Year,Month,Day,Hour,Minute,Second,DayOfWeek,PdDistrict,Address1,Address2,X,Y' Category gb 'n_estimators:i:10 learning_rate:f:0.1 max_depth:i:1 min_samples_leaf:i:40 random_state:i:0 verbose:i:1' ./pred log.txt cv

echo
echo '============================================================'
echo

echo 'end'
