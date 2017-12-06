# -*- coding : utf-8 -8-
#!/usr/bin/env python

__author__ = 'Toto Jiang'

import urllib2
import sys
import numpy as np
import pylab
import scipy.stats as stats

# read data
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data = urllib2.urlopen(target_url)

# arrange data
xList = []
labels = []

for line in data:
    row = line.strip().split(",")
    xList.append(row)
nrow = len(xList)
ncol = len(xList[1])

type = [0] * 3
colCounts = []

# generate summary statistics for column 3
col = 3
colData = []
for row in xList:
    colData.append(float(row[col]))

stats.probplot(colData, dist='norm', plot=pylab)
pylab.show()
