# coding=utf-8
__author__ = 'Nyunyunyunyu'

import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import SGD
from keras.utils.np_utils import to_categorical
import theano.tensor as T

def relu(x):
    return T.maximum(x, 0.)
T.nnet.relu = relu

train_set = pd.read_csv('../features/1_vector/train.csv', nrows=10000)
train_set = train_set[train_set.Y03 == 1]
category_num = 39#len(np.unique(train_set.Category))
train_set_category = to_categorical(train_set.Category, category_num)
train_set_vector = np.array(train_set.iloc[:, 1:])

model = Sequential()
model.add(Dense(output_dim=1000, input_dim=train_set_vector.shape[1], init="glorot_uniform"))
model.add(Activation("tanh"))
model.add(Dense(output_dim=500, init="glorot_uniform"))
model.add(Activation("tanh"))
model.add(Dense(output_dim=200, init="glorot_uniform"))
model.add(Activation("tanh"))
model.add(Dense(output_dim=category_num, init="glorot_uniform"))
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy', optimizer=SGD(lr=0.01, momentum=0.9, nesterov=True))

model.fit(train_set_vector, train_set_category, validation_split=0.5, batch_size=32, verbose=1)
