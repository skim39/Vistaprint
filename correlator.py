#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 12:19:47 2019

@author: carlfroneberger
"""

from sklearn.feature_selection import RFECV
from sklearn import linear_model, preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
import pyarrow.parquet as pq
import pandas as pd
import fastparquet
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import svm



data = pd.read_csv("colors_data.csv")
clf = svm.SVC(gamma='scale')
X = data[['OperatingSystem', 'GeoState', 'ShopperId']]
y = data[['attribute_name']]
clf.fit(X, y)  