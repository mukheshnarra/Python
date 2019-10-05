# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 08:55:35 2019

@author: MUKHESH
"""

import pandas as pd

l1=pd.Series([1,1],index={'index','olive'},name='fype')
l=pd.DataFrame({'image':l1,'question':['seelct','hello']},columns=['image','question'])
print(l.shape)
print(l.describe())
print(l.head())
l.columns=['mukhesh','names']
print(l.head())
