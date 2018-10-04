#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 21:49:23 2018

@author: jaimerson
"""

import pandas as pd
base = pd.read_csv('credit-data.csv')
base.describe()
base.loc[base['age'] < 0]