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
#apagar coluna
base.drop('age', 1, inplace=True)
#apagar apenas os registros com problemas
base.drop(base[base.age < 0].index, inplace=True)
#preencher manualmente os valores
#preencher os valores com a média
base.mean()
base['age'].mean()
base['age'][base.age > 0].mean()
base.loc[base.age < 0, 'age'] = base['age'][base.age > 0].mean()
pd.isnull(base['age'])
base.loc[pd.isnull(base['age'])]
