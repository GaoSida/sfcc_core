# param['objective'] = 'multi:softprob' always holds

#python boosting.py ./features/train_pool.csv ./features/test_pool.csv 'n_estimators:i:100 max_depth:i:8 learning_rate:f:0.1 silent:i:1 nthread:i:4 subsample:f:0.8 colsample_bytree:f:0.8 min_child_weight:i:5 gamma:f:0 reg_alpha:f:0.01' 'Year,Month,Day,Hour,Minute,Second,DayOfWeek,PdDistrict,X,Y' Category sub

python boosting.py ./features/train_pool.csv ./features/test_pool.csv 'n_estimators:i:200 max_depth:i:8 learning_rate:f:0.1 silent:i:1 nthread:i:4 colsample_bytree:f:0.8 subsample:f:0.8' 'Year,Month,Day,Hour,Minute,Second,DayOfWeek,PdDistrict,X,Y' Category cv

python boosting.py ./features/train_pool.csv ./features/test_pool.csv 'n_estimators:i:200 max_depth:i:8 learning_rate:f:0.1 silent:i:1 nthread:i:4 colsample_bytree:f:0.8 subsample:f:0.8' 'Year,Month,Day,Hour,Minute,Second,DayOfWeek,PdDistrict,X,Y' Category sub

#python boosting.py ./features/train_pool.csv ./features/test_pool.csv 'n_estimators:i:100 max_depth:i:8 min_child_weight:i:6 learning_rate:f:0.1 silent:i:1 nthread:i:4 subsample:f:0.8 colsample_bytree:f:0.8 gamma:f:0 reg_alpha:f:0.01' 'Year,Month,Day,Hour,Minute,Second,DayOfWeek,PdDistrict,X,Y' Category cv