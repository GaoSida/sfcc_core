#!/bin/bash

#python baselines.py rf_street_proba /2_street/train.csv /2_street/test.csv /2_street/fold_0.csv /2_street/fold_1.csv 'Year,Month,Day,Hour,Minute,Second,DayOfWeek,PdDistrict,Address1,Address2,X,Y,street_proba_0,street_proba_1,street_proba_2,street_proba_3,street_proba_4,street_proba_5,street_proba_6,street_proba_7,street_proba_8,street_proba_9,street_proba_10,street_proba_11,street_proba_12,street_proba_13,street_proba_14,street_proba_15,street_proba_16,street_proba_17,street_proba_18,street_proba_19,street_proba_20,street_proba_21,street_proba_22,street_proba_23,street_proba_24,street_proba_25,street_proba_26,street_proba_27,street_proba_28,street_proba_29,street_proba_30,street_proba_31,street_proba_32,street_proba_33,street_proba_34,street_proba_35,street_proba_36,street_proba_37,street_proba_38,street_proba_39' Category rf 'n_estimators:i:30 max_depth:i:8 min_samples_leaf:i:80 random_state:i:0 n_jobs:i:10 verbose:i:1' ./pred log.txt nsub

#python baselines.py rf_original /2_street/train.csv /2_street/test.csv /2_street/fold_0.csv /2_street/fold_1.csv 'Year,Month,Day,Hour,Minute,Second,DayOfWeek,PdDistrict,Address1,Address2,X,Y,street_proba_0,street_proba_1,street_proba_2,street_proba_3,street_proba_4,street_proba_5,street_proba_6,street_proba_7,street_proba_8,street_proba_9,street_proba_10,street_proba_11,street_proba_12,street_proba_13,street_proba_14,street_proba_15,street_proba_16,street_proba_17,street_proba_18,street_proba_19,street_proba_20,street_proba_21,street_proba_22,street_proba_23,street_proba_24,street_proba_25,street_proba_26,street_proba_27,street_proba_28,street_proba_29,street_proba_30,street_proba_31,street_proba_32,street_proba_33,street_proba_34,street_proba_35,street_proba_36,street_proba_37,street_proba_38,street_proba_39,street_sum' Category rf 'n_estimators:i:50 max_depth:i:10 min_samples_leaf:i:50 random_state:i:0 n_jobs:i:10 verbose:i:1' ./pred log.txt sub

python baselines.py rf_street_smooth_proba /2_street/train.csv /2_street/test.csv /2_street/fold_0.csv /2_street/fold_1.csv 'Year,Month,Day,Hour,Minute,Second,DayOfWeek,PdDistrict,Address1,Address2,X,Y,street_proba_0,street_proba_1,street_proba_2,street_proba_3,street_proba_4,street_proba_5,street_proba_6,street_proba_7,street_proba_8,street_proba_9,street_proba_10,street_proba_11,street_proba_12,street_proba_13,street_proba_14,street_proba_15,street_proba_16,street_proba_17,street_proba_18,street_proba_19,street_proba_20,street_proba_21,street_proba_22,street_proba_23,street_proba_24,street_proba_25,street_proba_26,street_proba_27,street_proba_28,street_proba_29,street_proba_30,street_proba_31,street_proba_32,street_proba_33,street_proba_34,street_proba_35,street_proba_36,street_proba_37,street_proba_38,street_proba_39,street_sum' Category rf 'n_estimators:i:50 max_depth:i:10 min_samples_leaf:i:50 random_state:i:0 n_jobs:i:10 verbose:i:1' ./pred log.txt sub