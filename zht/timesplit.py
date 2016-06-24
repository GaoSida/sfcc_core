# coding:utf-8
# 接收命令行参数的baseline实验框架


from sklearn import *
import numpy as np
import pandas as pd
import sys
import time
import pickle

feature_dir = '../features'
name2model = {
    'lr': linear_model.LogisticRegression,
    'rf': ensemble.RandomForestClassifier,
    'nb': naive_bayes.GaussianNB,
    'gb': ensemble.GradientBoostingClassifier
}

# 参数名:参数类型:参数值
columns = 'Year,Month,Day,Hour,Minute,Second,DayofWeek,PdDistrict,Address1,Address2,X,Y'
params = 'n_estimators:i:30 max_depth:i:8 min_samples_leaf:i:80 random_state:i:0 n_jobs:i:10 verbose:i:1'


def get_model_params(params_str):
    model_params = {}
    for param in params_str.split(" "):
        if len(param) == 0:
            continue
        tokens = param.split(':')
        k, t, v = tokens
        if t == 'f':
            v = float(v)
        elif t == 'i':
            v = int(v)
        elif t == 'b':
            v == True if v == 'True' else False
        elif t == 's':
            v = str(v)
        else:
            assert False, 'wrong type {}'.format(param)
        model_params[k] = v

    return model_params

# 两条竖线之间的是注释


def parseFeatureColumn(columns):
    columns = columns.split('|')
    column_index = []
    for c in range(len(columns)):
        if (c % 2 == 1):
            continue
        if len(columns[c]) == 0:
            continue
        c_list = columns[c].split(',')
        for i in c_list:
            if (len(i) == 0):
                continue
            column_index.append(i)
    return column_index

if __name__ == "__main__":

    current = str(int(time.time()))
    print "time " + current
    train_file = feature_dir + '/1_vector/train.csv'
    test_file = feature_dir + '/1_vector/test.csv'
    fold_0_file = feature_dir + '/1_vector/fold_0.csv'
    fold_1_file = feature_dir + '/1_vector/fold_1.csv'
    fea_cols = parseFeatureColumn(columns)
    target_col = 'Category'
    model_name = 'rf'
    model_params = params
    pred_dir = './pred'
    log_file = 'log.txt'
    mode = 'cv'

    model_params = get_model_params(model_params)

    exp_log = file(log_file, 'a')
    exp_log.write('Time: ' + current + '\n')
    exp_log.write('Train: ' + train_file + '\n' + 'Test: ' + test_file + '\n')
    exp_log.write('Fold 0: ' + fold_0_file + '\n' +
                  'Fold 1: ' + fold_1_file + '\n')
    exp_log.write('Feature: ' + str(fea_cols) + '\n' +
                  'Target: ' + target_col + '\n')
    exp_log.write('Model: ' + model_name +
                  " @params: " + str(model_params) + '\n')

    print 'loading fold_0...'
    df_fold_0 = pd.read_csv(fold_0_file)
    print 'loading fold_1...'
    df_fold_1 = pd.read_csv(fold_1_file)

    print 'start to extract features...'
    X_0 = df_fold_0[fea_cols].values
    Y_0 = df_fold_0[target_col].values
    X_1 = df_fold_1[fea_cols].values
    Y_1 = df_fold_1[target_col].values

    X_fold_0 = []
    X_fold_1 = []
    Y_fold_0 = []
    Y_fold_1 = []
    for i in range(len(X_0)):
        if X_0[i][0] < 2006:
            X_fold_0.append(X_0[0:i])
            X_fold_0.append(X_0[i + 1:])
            Y_fold_0.append(Y_0[0:i])
            Y_fold_0.append(Y_0[i + 1:])
            break

    for i in range(len(X_1)):
        if X_1[i][0] < 2006:
            X_fold_1.append(X_1[0:i])
            X_fold_1.append(X_1[i + 1:])
            Y_fold_1.append(Y_1[0:i])
            Y_fold_1.append(Y_1[i + 1:])
            break

    log_loss_0 = [0, 0]
    accuracy_0 = [0, 0]
    size_0 = [0, 0]
    for i in range(2):
        print 'start to train model with fold_0'
        model_0 = name2model[model_name](**model_params)
        model_0.fit(X_fold_0[i], Y_fold_0[i])

        print 'start to predict'
        Y_pred_prob = model_0.predict_proba(X_fold_1[i])
        Y_pred_label = model_0.predict(X_fold_1[i])
        log_loss_0[i] = metrics.log_loss(Y_fold_1[i], Y_pred_prob)
        accuracy_0[i] = metrics.accuracy_score(Y_fold_1[i], Y_pred_label)
        size_0[i] = len(Y_fold_0[i])
        # print log_loss_0[i]
    log_loss0 = log_loss_0[0] * size_0[0] + log_loss_0[1] * size_0[1]
    log_loss0 = log_loss0 / (size_0[0] + size_0[1])

    metric_0 = "LogLoss: " + str(log_loss0) + '\n'
    print metric_0
    exp_log.write(metric_0)

    log_loss_1 = [0, 0]
    accuracy_1 = [0, 0]
    size_1 = [0, 0]
    for i in range(2):
        print 'start to train model with fold_1'
        model_1 = name2model[model_name](**model_params)
        model_1.fit(X_fold_1[i], Y_fold_1[i])

        print 'start to predict'
        Y_pred_prob = model_1.predict_proba(X_fold_0[i])
        Y_pred_label = model_1.predict(X_fold_0[i])

        log_loss_1[i] = metrics.log_loss(Y_fold_0[i], Y_pred_prob)
        accuracy_1[i] = metrics.accuracy_score(Y_fold_0[i], Y_pred_label)
        size_1[i] = len(Y_fold_1[i])

    log_loss1 = log_loss_1[0] * size_1[0] + log_loss_1[1] * size_1[1]
    log_loss1 = log_loss1 / (size_1[0] + size_1[1])
    metric_1 = "LogLoss: " + str(log_loss1) + '\n'
    print metric_1
    exp_log.write(metric_1)

    print 'Average LogLoss: ' + str((log_loss0 + log_loss1) / 2)

    if (mode == 'sub'):
        print 'loading train file...'
        df_train = pd.read_csv(train_file)
        print 'loading test file...'
        df_test = pd.read_csv(test_file)

        print 'start to extract features...'
        X_train = df_train[fea_cols].values
        Y_train = df_train[target_col].values
        X_test = df_test[fea_cols].values

        model = name2model[model_name](**model_params)
        model.fit(X_train, Y_train)
        Y_pred_prob = model.predict_proba(X_test)

        Y_pred_prob = np.column_stack((range(len(Y_pred_prob)), Y_pred_prob))
        df_pred = pd.DataFrame(data=Y_pred_prob, columns='Id,ARSON,ASSAULT,BAD CHECKS,BRIBERY,BURGLARY,DISORDERLY CONDUCT,DRIVING UNDER THE INFLUENCE,DRUG/NARCOTIC,DRUNKENNESS,EMBEZZLEMENT,EXTORTION,FAMILY OFFENSES,FORGERY/COUNTERFEITING,FRAUD,GAMBLING,KIDNAPPING,LARCENY/THEFT,LIQUOR LAWS,LOITERING,MISSING PERSON,NON-CRIMINAL,OTHER OFFENSES,PORNOGRAPHY/OBSCENE MAT,PROSTITUTION,RECOVERED VEHICLE,ROBBERY,RUNAWAY,SECONDARY CODES,SEX OFFENSES FORCIBLE,SEX OFFENSES NON FORCIBLE,STOLEN PROPERTY,SUICIDE,SUSPICIOUS OCC,TREA,TRESPASS,VANDALISM,VEHICLE THEFT,WARRANTS,WEAPON LAWS'.split(','))

        print 'print submission...'
        df_pred[['Id']] = df_pred[['Id']].astype(int)
        df_pred.to_csv('../submissions/' + current + '.csv',
                       index=False, header=True, float_format='%.3f')

    exp_log.write(
        '\n=============================================================\n\n')
