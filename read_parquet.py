#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 11:04:15 2019

@author: ugoslight
"""
import pyarrow.parquet as pq
import pandas as pd
import fastparquet
data = pd.read_parquet("combokeywords.parquet", engine='fastparquet')#, engine='pyarrow')
#data.dtypes
