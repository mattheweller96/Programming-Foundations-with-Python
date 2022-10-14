# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:47:39 2021

@author: MREller
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 08:19:26 2021

@author: MREller
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.cluster.hierarchy import dendrogram, linkage
import sklearn
import seaborn as sns

netflix = pd.read_csv(r'C:\Users\MREller\PYTHON\netflix_titles.csv')

# Classification (Data Mining)

#print(list(netflix.columns.values))

netflix_class = netflix[netflix.columns[1:]]

#print(list(netflix_class.columns.values))

# Split data

test_idx = np.random.uniform(0, 1, len(netflix_class)) <= 0.333
train = netflix_class[test_idx == True]
test = netflix_class[test_idx == False]

#print(train.head())

#Analysis

