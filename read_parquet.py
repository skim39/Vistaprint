#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 11:04:15 2019

@author: ugoslight
"""
import pyarrow.parquet as pq
import pandas as pd
import fastparquet
data = pd.read_parquet("dataset.parquet", engine='fastparquet')#, engine='pyarrow')
data.set_index("Index", inplace=True)