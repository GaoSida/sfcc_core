#! /usr/bin/python
import pandas as pd
import numpy as np
import xgboost as xgb
from keras.utils.np_utils import to_categorical
import random
import time
import sys


def boosting_train(train_file, test_file, n_estimators, max_depth, learning_rate, nthread, task_type):
    if not task_type in ['cv', 'sub']:
        raise Exception('invalid task_type')
    # label need to be 0 to num_class -1
    train_set = pd.read_csv(train_file)

    # setup parameters for xgboost
    param = {}
    # use softmax multi-class classification
    param['objective'] = 'multi:softmax'
    param['n_estimators'] = n_estimators
    param['max_depth'] = max_depth
    param['learning_rate'] = learning_rate
    param['silent'] = 1
    param['nthread'] = nthread

    param['objective'] = 'multi:softprob'
    clf = xgb.XGBClassifier(**param)
    if task_type == "cv":
        grouped_data = train_set.groupby(lambda x: random.randint(0,1))

        train = grouped_data.get_group(0)
        test = grouped_data.get_group(1)

        train_X = train.iloc[:, 1:]
        train_Y = train.iloc[:, 0]

        test_X = test.iloc[:, 1:]
        test_Y = test.iloc[:, 0]
        clf.fit(train_X, train_Y, eval_set=[(train_X, train_Y),(test_X, test_Y)], eval_metric='mlogloss', verbose=True)
    elif task_type == "sub":
        x_train = train_set.iloc[:, 1:]
        y_train = train_set.iloc[:, 0]
        clf.fit(x_train, y_train, eval_set=[(x_train, y_train)], eval_metric='mlogloss', verbose=True)
        test_set = pd.read_csv(test_file).iloc[:,1:]

        Y_pred_prob = clf.predict_proba(test_set)
        Y_pred_prob = np.column_stack((range(len(Y_pred_prob)), Y_pred_prob))
        df_pred = pd.DataFrame(data=Y_pred_prob, columns='Id,ARSON,ASSAULT,BAD CHECKS,BRIBERY,BURGLARY,DISORDERLY CONDUCT,DRIVING UNDER THE INFLUENCE,DRUG/NARCOTIC,DRUNKENNESS,EMBEZZLEMENT,EXTORTION,FAMILY OFFENSES,FORGERY/COUNTERFEITING,FRAUD,GAMBLING,KIDNAPPING,LARCENY/THEFT,LIQUOR LAWS,LOITERING,MISSING PERSON,NON-CRIMINAL,OTHER OFFENSES,PORNOGRAPHY/OBSCENE MAT,PROSTITUTION,RECOVERED VEHICLE,ROBBERY,RUNAWAY,SECONDARY CODES,SEX OFFENSES FORCIBLE,SEX OFFENSES NON FORCIBLE,STOLEN PROPERTY,SUICIDE,SUSPICIOUS OCC,TREA,TRESPASS,VANDALISM,VEHICLE THEFT,WARRANTS,WEAPON LAWS'.split(','))

        current = str(int(time.time()))
        print 'print submission... filename: %s.csv' % current
        df_pred[['Id']] = df_pred[['Id']].astype(int)
        df_pred.to_csv('../submissions/' + current + '.csv', index=False, header=True, float_format='%.3f')

if __name__ == '__main__':
    if len(sys.argv) != 8:
        exit(-1)
    train_file = sys.argv[1]
    test_file = sys.argv[2]
    n_estimators = int(sys.argv[3])
    max_depth = int(sys.argv[4])
    learning_rate = float(sys.argv[5])
    nthread = int(sys.argv[6])
    task_type = sys.argv[7]
    boosting_train(train_file, test_file, n_estimators, max_depth, learning_rate, nthread, task_type)
