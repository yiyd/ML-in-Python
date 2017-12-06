#!/usr/bin/env python
# -*- coding: utf-8 -*- 
__author__ ="Toto Jiang"

import pandas as pd 
from pandas import DataFrame
from pylab import *
import matplotlib.pyplot as plot 

target_Url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data")

# read abalone data
abalone = pd.read_csv(target_Url, header=None, prefix="V")
abalone.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 
                    'Viscera weight', 'Shell weight', 'Rings']

print(abalone.head())
print(abalone.tail())

# print summary of data frame
summary = abalone.describe()
print(summary)

# box plot the real-valued attribute
array = abalone.iloc[:, 1:9].values
boxplot(array)
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Ranges")
plot.show()

# the last column is out of scale
array = abalone.iloc[:, 1:8].values
boxplot(array)
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Ranges")
plot.show()

# 对属性值进行归一化处理
abaloneNormalized = abalone.iloc[:, 1:9]

for i in range(8):
    mean = summary.iloc[1, i]
    sd = summary.iloc[2, i]
    abaloneNormalized.iloc[:, i:(i+1)] = (abaloneNormalized.iloc[:, i:(i+1)] - mean) / sd

array3 = abaloneNormalized.values
boxplot(array3)
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Ranges - Normalized")
plot.show()




