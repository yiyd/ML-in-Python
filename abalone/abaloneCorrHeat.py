#!/bin/env python
# -*- coding : utf-8 -*-

__author__ = 'Toto Jiang'

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

target_Url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data")

# read data
abalone = pd.read_csv(target_Url, header=None, prefix='V')
abalone.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight',
                    'Viscera weight', 'Shell weight', 'Rings']

# calculate correlation matrix
#print(abalone.iloc[0:1, 1:9])
cor_mat = DataFrame(abalone.iloc[:, 1:9].corr())
print(cor_mat)

# using heatmap
plot.pcolor(cor_mat)
plot.show()

