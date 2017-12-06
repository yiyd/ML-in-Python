#!/usr/bin/env python
# -*- coding: utf-8 -*- 
__author__ ="Toto Jiang"

import pandas as pd 
from pandas import DataFrame
import matplotlib.pyplot as plot 
from math import exp

target_Url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data")

# read data
abalone = pd.read_csv(target_Url, header=None, prefix='v')
abalone.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight',
                   'Viscera weight', 'Shell weight', 'Rings']

# get summary to use for scaling
summary = abalone.describe()
print(summary)
minRings = summary.iloc[3, 7]
maxRings = summary.iloc[7, 7]
nrows = len(abalone.index)

for i in range(nrows):
    # plot rows of data
    dataRow = abalone.iloc[i, 1:8]
    labelColor = (abalone.iloc[i, 8] - minRings) / (maxRings - minRings)
    dataRow.plot(color=plot.cm.RdYlBu(labelColor), alpha=0.5)

plot.xlabel("Attribute Index")
plot.ylabel("Attribute Values")
plot.show()

# renormalize using mean and standard variation
meanRings = summary.iloc[1, 7]
sdRings = summary.iloc[2, 7]

for i in range(nrows):
    # plot rows data
    dataRow = abalone.iloc[i, 1:8]
    normTarget = (abalone.iloc[i, 8] - meanRings) / sdRings
    labelColor = 1.0 / (1.0 + exp(-normTarget))
    dataRow.plot(color=plot.cm.RdYlBu(labelColor), alpha=0.5)

plot.xlabel("Attribute Index")
plot.ylabel("Attribute Values")
plot.show()
