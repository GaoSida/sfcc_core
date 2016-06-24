from sklearn import *
import numpy as np
import pandas as pd
#from keras.utils.np_utils import to_categorical
import random
import xgboost as xgb


#XX = pd.read_csv('test.txt')
#grouped_data = XX.groupby(lambda x: random.randint(0, 5))
#train = grouped_data.get_group(3)
#test = grouped_data.get_group(1)

#print (train)
# print test
name2model = {
    'lr': linear_model.LogisticRegression,
    'rf': ensemble.RandomForestClassifier,
    'nb': naive_bayes.GaussianNB,
    'gb': ensemble.GradientBoostingClassifier,
    'knn': neighbors.KNeighborsClassifier,
    'xgb': xgb.XGBClassifier
}

param = {}
# use softmax multi-class classification
param['objective'] = 'multi:softmax'
param['n_estimators'] = 100
param['max_depth'] = 8
param['learning_rate'] = 0.1
param['silent'] = 1
param['nthread'] = 2
param['objective'] = 'multi:softprob'


#X1 = np.array([[1, 2, 1, 0], [1, 1, 1, 0], [
#              1, 3, 1, 2], [4, 5, 1, 1], [5, 6, 2, 1]])
#X2 = np.array([[1, 3, 1, 0], [1, 2, 1, 0], [
#              1, 1, 5, 1], [4, 4, 1, 2], [5, 3, 2, 1], [1, 2, 3, 2]])
X1 = X2 = pd.read_csv('test.txt')
train_X = X1.iloc[:, 1:]
train_Y = X1.iloc[:, 0]
test_X = X2.iloc[:, 1:]
test_Y = X2.iloc[:, 0]
print (train_X)
print (train_Y)

clf = name2model['lr']()
clf.fit(train_X, train_Y)
Y_pred_prob = clf.predict_proba(test_X)
print(Y_pred_prob)
Y_pred_label = clf.predict(test_X)
print(Y_pred_label)

print ('===================================================')

xg_train = xgb.DMatrix(train_X, label=train_Y)
xg_test = xgb.DMatrix(test_X, label=test_Y)
# setup parameters for xgboost
param = {}
# use softmax multi-class classification
param['objective'] = 'multi:softmax'
# scale weight of positive examples
param['eta'] = 0.1
param['max_depth'] = 6
param['silent'] = 1
param['nthread'] = 4
param['num_class'] = 6

watchlist = [(xg_train, 'train'), (xg_test, 'test')]
num_round = 1
bst = xgb.train(param, xg_train, num_round, watchlist)
# get prediction
pred = bst.predict(xg_test)

print('predicting, classification error=%f' % (
    sum(int(pred[i]) != test_Y[i] for i in range(len(test_Y))) / float(len(test_Y))))

# do the same thing again, but output probabilities
param['objective'] = 'multi:softprob'
bst = xgb.train(param, xg_train, num_round, watchlist)
# Note: this convention has been changed since xgboost-unity
# get prediction, this is in 1D array, need reshape to (ndata, nclass)
yprob = bst.predict(xg_test).reshape(test_Y.shape[0], -1)
print(yprob)
ylabel = np.argmax(yprob, axis=1)

print('predicting, classification error=%f' % (sum(
    int(ylabel[i]) != test_Y[i] for i in range(len(test_Y))) / float(len(test_Y))))
