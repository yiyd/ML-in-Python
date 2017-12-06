# -*- coding: utf-8 -*-
#!/usr/bin/evn python

__author__ = 'Toto Jiang'

import urllib2
import sys
import numpy as np

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

colArray = np.array(colData)
colMean = np.mean(colArray)
colsd = np.std(colArray)
sys.stdout.write("Mean = " + '\t' + str(colMean) + '\t\t' + "Standard Deviation = " + '\t' + str(colsd) + '\n')

# calculate quantile boundaries
ntiles = 4

percnetBdry = []

for i in range(ntiles + 1):
    percnetBdry.append(np.percentile(colArray, i * (100) / ntiles))

sys.stdout.write("\nBoundaries for 4 Equal Percentiles \n")
print(percnetBdry)
sys.stdout.write(" \n")

# run again with 10 equal intervals
ntiles = 10

percnetBdry = []

for i in range(ntiles + 1):
    percnetBdry.append(np.percentile(colArray, i * (100) / ntiles))

sys.stdout.write("\nBoundaries for 10 Equal Percentiles \n")
print(percnetBdry)
sys.stdout.write(" \n")

# The last column contains categorical variables
col = 60
colData = []
for row in xList:
    colData.append(row[col])

unique = set(colData)
sys.stdout.write("Unique Label Values \n")
print(unique)

# count up the number of elements having each value
catDict = dict(zip(list(unique), range(len(unique))))
catCount = [0] * 2

for elt in colData:
    catCount[catDict[elt]] += 1

sys.stdout.write("\nCounts for Each Value of Categorical Label \n")
print(list(unique))
print(catCount)
