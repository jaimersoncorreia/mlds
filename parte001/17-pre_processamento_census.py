#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 20:24:43 2018

@author: jaimerson
"""

import pandas as pd
base = pd.read_csv('census.csv')

#dividir a base em previsores e classe
previsores = base.iloc[:, 0:14].values
classe = base.iloc[:,14].values

#traformar dados string para dados em numéricos
from sklearn.preprocessing import LabelEncoder
labelencoder_previsores = LabelEncoder()
#labels = labelencoder_previsores.fit_transform(previsores[:, 1])

previsores[:,1]= labelencoder_previsores.fit_transform(previsores[:, 1])
previsores[:,3]= labelencoder_previsores.fit_transform(previsores[:, 3])
previsores[:,5]= labelencoder_previsores.fit_transform(previsores[:, 5])
previsores[:,6]= labelencoder_previsores.fit_transform(previsores[:, 6])
previsores[:,7]= labelencoder_previsores.fit_transform(previsores[:, 7])
previsores[:,8]= labelencoder_previsores.fit_transform(previsores[:, 8])
previsores[:,9]= labelencoder_previsores.fit_transform(previsores[:, 9])
previsores[:,13]= labelencoder_previsores.fit_transform(previsores[:, 13])

previsores