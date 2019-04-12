#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 13:08:52 2019

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


data = pd.read_csv("small.csv")
data.dropna()
pca = PCA(n_components=4)
pca.fit(data)
