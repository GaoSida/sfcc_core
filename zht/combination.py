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
params_rf = 'min_samples_leaf:i:20 n_estimators:i:40 random_state:i:0 max_depth:i:14'
params_xgb = 'n_estimators:i:100 max_depth:i:8 learning_rate:f:0.1'


def model_train(train_file, test_file, model, task_type):

    train_set = pd.read_csv(feature_dir + train_file)
    test_set = pd.read_csv(feature_dir + test_file)
    # setup parameters for xgboost
    param = {}
    if model == 'xgb':
        # use softmax multi-class classification
        param['objective'] = 'multi:softmax'
        param['n_estimators'] = 200
        param['max_depth'] = 8
        param['min_child_weight'] = 5
        param['learning_rate'] = 0.08
        param['silent'] = 1
        param['nthread'] = 24
        param['colsample_bytree'] = 0.8
        param['subsample'] = 0.8
        param['gamma'] = 0
        param['reg_alpha'] = 0.01
        param['objective'] = 'multi:softprob'
    elif model == 'rf':
        param['min_samples_leaf'] = 20
        param['n_estimators'] = 40
        param['random_state'] = 0
        param['max_depth'] = 14
        # clf = xgb.XGBClassifier(**param)
    clf = name2model[model](**param)
    if task_type == "cv":

        train_X = train_set.iloc[:1000, 1:]
        train_Y = train_set.iloc[:1000, 0]
        test_X = test_set.iloc[:1000, 1:]
        test_Y = test_set.iloc[:1000, 0]
        clf.fit(train_X, train_Y)
        
        Y_pred_prob = clf.predict_proba(test_X)
        print (Y_pred_prob)
        Y_pred_label = clf.predict(test_X)
        #print (Y_pred_label)

        logloss = metrics.log_loss(test_Y, Y_pred_prob)
        accuracy = metrics.accuracy_score(test_Y, Y_pred_label)
        print(logloss)
        return Y_pred_prob


def combine_train(res_fea, train_file, test_file, model, task_type):

    train_set = pd.read_csv(feature_dir + train_file)
    test_set = pd.read_csv(feature_dir + test_file)
    clf = name2model[model]()
    if task_type == 'cv':

        train_X = res_fea
        train_Y = train_set.iloc[:, 0]
        test_X = test_set.iloc[:, 1:]
        test_Y = test_set.iloc[:, 0]
        clf.fit(train_X, train_Y)
        Y_pred_prob = clf.predict_proba(test_X)
        # print Y_pred_prob
        Y_pred_label = clf.predict(test_X)

        logloss = metrics.log_loss(test_Y, Y_pred_prob)
        accuracy = metrics.accuracy_score(test_Y, Y_pred_label)
        print(logloss)

if __name__ == '__main__':

    res_train = []
    res_train_rf = model_train(
        'fold_0.csv', 'fold_0.csv', 'rf', 'cv')
    res_train_xgb = model_train(
        'fold_0.csv', 'fold_0.csv', 'xgb', 'cv')
    #res_fea.extend(res_rf)
    #res_fea.extend(res_xgb)
