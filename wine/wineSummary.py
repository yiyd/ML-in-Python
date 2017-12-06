#!/bin/env python
# -*- coding : utf-8 -*-

__author__ = 'Toto Jiang'

import pandas as pd
from pandas import DataFrame
from pylab import *
import matplotlib.pyplot as plot

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv")
wine = pd.read_csv(target_url, header=0, sep=";")

print(wine.head())