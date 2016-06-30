python baselines.py knn_direct /0_direct/train.csv /0_direct/test.csv /4_points/fold_0.csv /4_points/fold_1.csv 'Month,Hour,X,Y' Category knn 'n_neighbors:i:3000 weights:s:uniform algorithm:s:kd_tree n_jobs:i:4' ./pred knn.txt cv

python baselines.py knn_direct /0_direct/train_norm.csv /0_direct/test_norm.csv /4_points/fold_0.csv /4_points/fold_1.csv 'Month,Hour,X,Y' Category knn 'n_neighbors:i:3000 weights:s:uniform algorithm:s:kd_tree n_jobs:i:4' ./pred knn.txt cv

python baselines.py knn_direct /0_direct/train.csv /0_direct/test.csv /4_points/fold_0.csv /4_points/fold_1.csv 'Month,Hour,X,Y' Category knn 'n_neighbors:i:3000 weights:s:uniform algorithm:s:kd_tree n_jobs:i:4' ./pred knn.txt sub

python baselines.py knn_direct /0_direct/train_norm.csv /0_direct/test_norm.csv /4_points/fold_0.csv /4_points/fold_1.csv 'Month,Hour,X,Y' Category knn 'n_neighbors:i:3000 weights:s:uniform algorithm:s:kd_tree n_jobs:i:4' ./pred knn.txt sub