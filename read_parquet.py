#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 11:04:15 2019
Use a.empty, a.bool(), a.item(), a.any() or a.all().
@author: ugoslight
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

"""Suppress a warning and init label encoder"""
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")
label_encode = preprocessing.LabelEncoder()

"""Load dataset"""
data = pd.read_parquet("dataset.parquet", engine='fastparquet')
design_data = pd.read_parquet("comboattributes.parquet", engine='fastparquet')
category_data = pd.read_parquet("combocategories.parquet", engine='fastparquet')

"""Smaller data frame for testing and building"""
data = data.iloc[ 0:100000 , : ]

"""Check for missing data in all columns and all rows, return dictionary of number of missing
values in a column"""
missing_dict = {}
for ele in data.columns:
    missing_dict.update({ele: 0}) #Declare 0 for all missing elements in every column
    
for row in range(0, len(data)):
    for ele in data.columns:
        if data.at[row, ele] == '':
            missing_dict[ele] += 1;
        
"""Label encode columns with strings"""
for ele in data.columns: 
    for row in range(0, len(data)):
        if type(data.at[row, ele]) == str:
            label_encode.fit(data[ele])
            data[ele] = label_encode.transform(data[ele])
            break

        
"""Feature matrix and target vector"""
X = data.iloc[0:100000, [0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26]]
y = data.iloc[0:100000,[15]]


"""Model and recursive feature elimination
model = linear_model.LinearRegression()
rfecv = RFECV(estimator=model, step=1, scoring='neg_mean_squared_error')
rfecv.fit(X, y)
rfecv.transform(X)
rfecv.n_features_
rfecv.poof()"""
"""Split data into training and test"""
X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    test_size=0.3, 
                                                    random_state=1)
"""Standardize features apply to both training and test"""
standardizer = StandardScaler()
standardizer.fit(X_train)
X_train_std = standardizer.transform(X_train)
X_test_std = standardizer.transform(X_test)

"""Create logistic regression object using sag solver"""
clf = LogisticRegression(random_state=0, solver='sag')
"""Logistic regression model"""
model = clf.fit(X_std, y)