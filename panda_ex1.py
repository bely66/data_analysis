# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:14:41 2019

@author: USER
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import panfun as pf
d = {"nabil":1000,"ahmed":100,"mar":500,"yassin":1500,"mari":15,"as":45,"saas":15000}

data = pf.return_series_rng(d,20,1100)
print(data)