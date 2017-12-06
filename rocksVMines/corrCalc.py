#!/usr/bin/env python
# -*- coding : utf-8 -*-

__author__ = "Toto Jiang" 

import pandas as pd 
from pandas import DataFrame
from math import sqrt
import sys

target_url = (
    "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

dataRow2 = rocksVMines.iloc[1, 0:60]
dataRow3 = rocksVMines.iloc[2, 0:60]
dataRow21 = rocksVMines.iloc[20, 0:60]

mean2 = 0.0; mean3 = 0.0; mean21 = 0.0
numElt = len(dataRow2)
for i in range(numElt):
    mean2 += dataRow2[i] / numElt
    mean3 += dataRow3[i] / numElt
    mean21 += dataRow21[i] / numElt

var2 = 0.0; var3 = 0.0; var21 = 0.0
for i in range(numElt):
    var2 += (dataRow2[i] - mean2) * (dataRow2[i] - mean2) / numElt
    var3 += (dataRow3[i] - mean3) * (dataRow3[i] - mean3) / numElt
    var21 += (dataRow21[i] - mean21) * (dataRow21[i] - mean21) / numElt

corr_2_3 = 0.0; corr_2_21 = 0.0
for i in range(numElt):
     corr_2_3 += (dataRow2[i] - mean2) * (dataRow3[i] - mean3) / (sqrt(var2 * var3) * numElt)
     corr_2_21 += (dataRow2[i] - mean2) * (dataRow21[i] - mean21) / (sqrt(var2 * var21) * numElt)

sys.stdout.write("Correlation between attribute 2 and 3 \n")
print(corr_2_3)
sys.stdout.write("Correlation between attribute 2 and 21 \n")
print(corr_2_21)