#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Toto Jiang"

import pandas as pd 
from pandas import DataFrame
import matplotlib.pylab as plot
from random import uniform

target_url = (
    "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

# change the targets to numeric values
target = []
for i in range(208):
    # assign 0 or 1 target value based on "M" or "R" labels
    if rocksVMines.iat[i, 60] == "M":
        target.append(1.0)
    else:
        target.append(0.0)

# plot 35 attributes
dataRow = rocksVMines.iloc[0:208, 35]
plot.scatter(dataRow, target)

plot.xlabel("Attribute Value")
plot.ylabel("Target Value")
plot.show()

# 
# Improve the visualization, this version dithers the points a little
target = []
for i in range(208):
    if rocksVMines.iat[i, 60] == "M":
        target.append(1.0 + uniform(-0.1, 0.1))
    else:
        target.append(0.0 + uniform(-0.1, 0.1))

dataRow = rocksVMines.iloc[0:208, 35]
plot.scatter(dataRow, target, alpha=0.5, s=20)
plot.xlabel("Attribute Value")
plot.ylabel("Target Value")
plot.show()
