# -*- coding : utf-8 -8-
#!/usr/bin/env python

__author__ = 'Toto Jiang'

import pandas as pd 
from pandas import DataFrame
import matplotlib.pylab as plot
import os

# read data
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

# read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

print(rocksVMines.head())
print(rocksVMines.tail())

# print summary of data frame
summary = rocksVMines.describe()
print(summary)





