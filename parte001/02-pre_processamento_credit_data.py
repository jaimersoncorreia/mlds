#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 21:49:23 2018

@author: jaimerson
"""
import pandas as pd
base = pd.read_csv('credit-data.csv')

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

previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4]
#tratamento do valores faltantes
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(previsores[:, 0:3])
previsores[:, 0:3]= imputer.transform(previsores[:,0:3])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)