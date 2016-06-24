from sklearn import *
import numpy as np
import pandas as pd
import xgboost as xgb
import sys
import time
import pickle

feature_dir = '../features/0_direct/'
name2model = {
    'lr': linear_model.LogisticRegression,
    'rf': ensemble.RandomForestClassifier,
    'nb': naive_bayes.GaussianNB,
    'gb': ensemble.GradientBoostingClassifier,
    'knn': neighbors.KNeighborsClassifier,
    'xgb': xgb.XGBClassifier
}
param_xgb = {}
#param_xgb['objective'] = 'multi:softmax'
param_xgb['n_estimators'] = 200
param_xgb['max_depth'] = 8
param_xgb['min_child_weight'] = 5
param_xgb['learning_rate'] = 0.08
param_xgb['silent'] = 1
param_xgb['nthread'] = 2
param_xgb['colsample_bytree'] = 0.8
param_xgb['subsample'] = 0.8
param_xgb['gamma'] = 0
param_xgb['reg_alpha'] = 0.01
param_xgb['objective'] = 'multi:softprob'

param_rf = {}
param_rf['min_samples_leaf'] = 20
param_rf['n_estimators'] = 40
param_rf['random_state'] = 0
param_rf['max_depth'] = 14


def combine_train(train_file, test_file):

    train_set = pd.read_csv(feature_dir + train_file)
    test_set = pd.read_csv(feature_dir + test_file)
    train_X = train_set.iloc[:10000, 1:]
    train_Y = train_set.iloc[:10000, 0]
    test_X = test_set.iloc[:10000, 1:]
    test_Y = test_set.iloc[:10000, 0]

    model_rf = name2model['rf'](**param_rf)
    model_rf.fit(train_X, train_Y)
    Y_prob_rf = model_rf.predict_proba(train_X)

    model_xgb = name2model['xgb'](**param_xgb)
    model_xgb.fit(train_X, train_Y)
    Y_prob_xgb = model_xgb.predict_proba(train_X)

    print(Y_prob_rf.shape[1])
    print(Y_prob_xgb.shape[1])
    combine_prob = np.append(Y_prob_rf, Y_prob_xgb, 1)
    print(combine_prob.shape)
    print(train_Y.shape)

    model_lr = name2model['lr']()
    model_lr.fit(combine_prob, train_Y)

    Y_prob_rf = model_rf.predict_proba(test_X)
    logloss_rf = metrics.log_loss(test_Y, Y_prob_rf)
    print(logloss_rf)
    Y_prob_xgb = model_xgb.predict_proba(test_X)
    logloss_xgb = metrics.log_loss(test_Y, Y_prob_xgb)
    print(logloss_xgb)

    combine_prob = np.append(Y_prob_rf, Y_prob_xgb, 1)
    Y_prob_comb = model_lr.predict_proba(combine_prob)
    logloss_comb = metrics.log_loss(test_Y, Y_prob_comb)
    print(logloss_comb)

if __name__ == '__main__':

    combine_train('fold_0.csv', 'fold_1.csv')
