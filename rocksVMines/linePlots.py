# -*- coding : utf-8 -8-
#!/usr/bin/env python

__author__ = 'Toto Jiang'

import pandas as pd    
from pandas import DataFrame
import matplotlib.pylab as plot

# read data
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

for i in range(208):
    # assign color
    if rocksVMines.iat[i, 60] == "M":
        pcolor = "red"
    else:
        pcolor = "blue"
    
    dataRow = rocksVMines.iloc[i, 0:60]
    dataRow.plot(color=pcolor)

plot.xlabel("Attribute Index")
plot.ylabel("Attribute Values")
plot.show()