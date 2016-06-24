#!/bin/bash

#python baselines.py rf_direct_feature /1_vector/train.csv /1_vector/test.csv /1_vector/fold_0.csv /1_vector/fold_1.csv 'Y03,Y04,Y05,Y06,Y07,Y08,Y09,Y10,Y11,Y12,Y13,Y14,Y15,M1,M2,M3,M4,M5,M6,M7,M8,M9,M10,M11,M12,D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12,D13,D14,D15,D16,D17,D18,D19,D20,D21,D22,D23,D24,D25,D26,D27,D28,D29,D30,D31,H0,H1,H2,H3,H4,H5,H6,H7,H8,H9,H10,H11,H12,H13,H14,H15,H16,H17,H18,H19,H20,H21,H22,H23,Year,Month,Day,Hour,Minute,Second,DayofWeek,W1,W2,W3,W4,W5,W6,W7,PdDistrict,Pd1,Pd2,Pd3,Pd4,Pd5,Pd6,Pd7,Pd8,Pd9,Pd10,Address1,Address2,X,Y' Category rf 'n_estimators:i:50 max_depth:i:12 min_samples_leaf:i:30 random_state:i:0 n_jobs:i:10 verbose:i:1' ./pred log.txt nsub

#python baselines.py rf_direct_feature /1_vector/train.csv /1_vector/test.csv /1_vector/fold_0.csv /1_vector/fold_1.csv 'Y03,Y04,Y05,Y06,Y07,Y08,Y09,Y10,Y11,Y12,Y13,Y14,Y15,M1,M2,M3,M4,M5,M6,M7,M8,M9,M10,M11,M12,D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12,D13,D14,D15,D16,D17,D18,D19,D20,D21,D22,D23,D24,D25,D26,D27,D28,D29,D30,D31,Hour,Minute,Second,W1,W2,W3,W4,W5,W6,W7,PdDistrict,Address1,Address2,X,Y' Category rf 'n_estimators:i:30 max_depth:i:8 min_samples_leaf:i:80 random_state:i:0 n_jobs:i:10 verbose:i:1' ./pred log.txt sub

python baselines.py rf_pd2bin /1_vector/train.csv /1_vector/test.csv /1_vector/fold_0.csv /1_vector/fold_1.csv 'Pd1,Pd2,Pd3,Pd4,Pd5,Pd6,Pd7,Pd8,Pd9,Pd10,Year,Month,Day,Hour,Minute,Second,DayofWeek,Address1,Address2,X,Y' Category rf 'n_estimators:i:30 max_depth:i:8 min_samples_leaf:i:80 random_state:i:0 n_jobs:i:10 verbose:i:1' ./pred log.txt nsub

