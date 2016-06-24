

python baselines.py knn_direct /0_direct/train.csv /0_direct/test.csv /0_direct/fold_0.csv /0_direct/fold_1.csv 'Month,Hour,X,Y' Category knn 'n_neighbors:i:2000 weights:s:uniform algorithm:s:kd_tree n_jobs:i:4' ./pred knn.txt nsub