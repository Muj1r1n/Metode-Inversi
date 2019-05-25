#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 10:11:51 2019

@author: thomas
"""
from inversi import plot, matrikG, matrikM
import numpy as np
import pandas as pd

def predict(z):
    x1 = list(np.ones(len(z)))
    z2 = list(np.array(z)**2)
    x2 = z
    x3 = z2
    list_data = [x1, x2, x3]
    G = matrikG(list_data)

    m = matrikM(G, T)
    prediksi = []
    for i in range(len(z)):
        y = m[0] + m[1]*x1[i] + m[2]*x2[i]**2
        prediksi.append(y)
    return prediksi


# Inversi Model Parabola
# =============================================================================
z = [5, 8, 14, 21, 30, 36, 45, 60]
T = [21.75, 22.68, 25.62, 30.87, 40.5, 48.72, 63.75, 96]
# Gambar
plot(z, T)
# Parameter hasil perhitungan m
# [21.000000000000135, 0.049999999999986056, 0.0200000000000001]


prediksi = predict(z)
df = pd.DataFrame()
df['Kedalaman (m)'] = z
df['Temp. pengukuran (T)'] = T
df['Temp. prediksi (T)'] = prediksi

print(df)
