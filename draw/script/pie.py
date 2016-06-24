# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will
# list the files in the input directory
# Any results you write to the current directory are saved as output.

import seaborn as sns
import matplotlib.pyplot as plt

crimeData = pd.read_csv('../input/train.csv')
print(crimeData.shape)

CategoryData = pd.DataFrame(crimeData['Category'].value_counts())
print CategoryData

Category = CategoryData.iloc[:10, :]

print Category

plt.figure(figsize=(16, 10))

# 对前10位的犯罪类型绘制饼图
plt.pie(Category, labels=Category.index)

# plt.show()
plt.savefig('pie.png')
