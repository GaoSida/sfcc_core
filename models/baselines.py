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
        'gb': ensemble.GradientBoostingClassifier,
        'knn': neighbors.KNeighborsClassifier
        }

# 参数名:参数类型:参数值
def get_model_params(params_str):
    model_params = {}
    for param in params_str.split(" "):
        if len(param) == 0: continue
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
    if len(sys.argv) != 13:
        print 'Usage: {} alias train_file test_file fold_0_file fold_1_file feature_cols label_col model_type model_params pred_dir log_file mode'.format(sys.argv[0])
        sys.exit(0)

    current = str(int(time.time()))
    alias = sys.argv[1]
    print "time " + current + ', ' + alias
    train_file = feature_dir + sys.argv[2]
    test_file = feature_dir + sys.argv[3]
    fold_0_file = feature_dir + sys.argv[4]
    fold_1_file = feature_dir + sys.argv[5]
    fea_cols = parseFeatureColumn(sys.argv[6])
    target_col = sys.argv[7]
    model_name = sys.argv[8]
    model_params = sys.argv[9]
    pred_dir = sys.argv[10]
    log_file = sys.argv[11]
    mode = sys.argv[12]

    model_params = get_model_params(model_params)

    exp_log = file(log_file, 'a')
    exp_log.write('Time: ' + current + '\n')
    exp_log.write('Alias: ' + alias + '\n')
    exp_log.write('Train: ' + train_file + '\n' + 'Test: ' + test_file + '\n')
    exp_log.write('Fold 0: ' + fold_0_file + '\n' + 'Fold 1: ' + fold_1_file + '\n')
    exp_log.write('Feature: ' + str(fea_cols) + '\n' + 'Target: ' + target_col + '\n')
    exp_log.write('Model: ' + model_name + " @params: " + str(model_params) + '\n')

    if (mode != 'sub'):
        print 'loading fold_0...'
        df_fold_0 = pd.read_csv(fold_0_file)
        print 'loading fold_1...'
        df_fold_1 = pd.read_csv(fold_1_file)

        print 'start to extract features...'
        X_fold_0  = df_fold_0[fea_cols].values
        Y_fold_0 = df_fold_0[target_col].values
        X_fold_1 = df_fold_1[fea_cols].values
        Y_fold_1 = df_fold_1[target_col].values

        print 'start to train model with fold_0'
        model_0 = name2model[model_name](**model_params)
        model_0.fit(X_fold_0, Y_fold_0)

        print 'start to predict'
        Y_pred_prob = model_0.predict_proba(X_fold_1)
        Y_pred_label = model_0.predict(X_fold_1)

        logloss_0 = metrics.log_loss(Y_fold_1, Y_pred_prob)
        accuracy_0 = metrics.accuracy_score(Y_fold_1, Y_pred_label)
        metric_0 = "LogLoss: " + str(logloss_0) + " Accuracy: " + str(accuracy_0) + '\n'
        print metric_0
        exp_log.write(metric_0)

        print 'start to train model with fold_1'
        model_1 = name2model[model_name](**model_params)
        model_1.fit(X_fold_1, Y_fold_1)

        print 'start to predict'
        Y_pred_prob = model_1.predict_proba(X_fold_0)
        Y_pred_label = model_1.predict(X_fold_0)

        logloss_1 = metrics.log_loss(Y_fold_0, Y_pred_prob)
        accuracy_1 = metrics.accuracy_score(Y_fold_0, Y_pred_label)
        metric_1 = "LogLoss: " + str(logloss_1) + " Accuracy: " + str(accuracy_1) + '\n'
        print metric_1
        exp_log.write(metric_1)

        print 'Average LogLoss: ' + str((logloss_0 + logloss_1) / 2)

    if (mode == 'sub'):
        print 'loading train file...'
        df_train = pd.read_csv(train_file)
        print 'loading test file...'
        df_test = pd.read_csv(test_file)

        print 'start to extract features...'
        X_train  = df_train[fea_cols].values
        Y_train = df_train[target_col].values
        X_test = df_test[fea_cols].values

        model = name2model[model_name](**model_params)
        model.fit(X_train, Y_train)
        Y_pred_prob = model.predict_proba(X_test)

        Y_pred_prob = np.column_stack((range(len(Y_pred_prob)), Y_pred_prob))
        df_pred = pd.DataFrame(data=Y_pred_prob, columns='Id,ARSON,ASSAULT,BAD CHECKS,BRIBERY,BURGLARY,DISORDERLY CONDUCT,DRIVING UNDER THE INFLUENCE,DRUG/NARCOTIC,DRUNKENNESS,EMBEZZLEMENT,EXTORTION,FAMILY OFFENSES,FORGERY/COUNTERFEITING,FRAUD,GAMBLING,KIDNAPPING,LARCENY/THEFT,LIQUOR LAWS,LOITERING,MISSING PERSON,NON-CRIMINAL,OTHER OFFENSES,PORNOGRAPHY/OBSCENE MAT,PROSTITUTION,RECOVERED VEHICLE,ROBBERY,RUNAWAY,SECONDARY CODES,SEX OFFENSES FORCIBLE,SEX OFFENSES NON FORCIBLE,STOLEN PROPERTY,SUICIDE,SUSPICIOUS OCC,TREA,TRESPASS,VANDALISM,VEHICLE THEFT,WARRANTS,WEAPON LAWS'.split(','))

        print 'print submission...'
        df_pred[['Id']] = df_pred[['Id']].astype(int)
        df_pred.to_csv('../submissions/' + current + '.csv', index=False, header=True, float_format='%.3f')

    exp_log.write('\n=============================================================\n\n')


