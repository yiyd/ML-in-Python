__author__ = "Toto Jiang"

import pandas as pd 
from pandas import DataFrame
import matplotlib.pylab as plot

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

# calculate correlations 
dataRow2 = rocksVMines.iloc[1, 0:60]
print(str(len(dataRow2)))
dataRow3 = rocksVMines.iloc[2, 0:60]

plot.scatter(dataRow2, dataRow3)
plot.xlabel("2nd Attribute")
plot.ylabel("3rd Attribute")
plot.show()
