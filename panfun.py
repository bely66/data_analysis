# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:44:25 2019

@author: USER
"""
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

def return_series(d):
    series = pd.Series(d)
    return series 

def return_series_rng (d ,x , y):
    series = pd.Series(d)
    series = series [series<y]
    series = series [series>x]
    return series

def find_word (d,s):
    series = pd.Series(d)
    return series[s]
