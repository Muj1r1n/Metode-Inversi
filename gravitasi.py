#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 10:12:23 2019

@author: Mujirin|mujirin@ui.ac.id
"""
from inversi import plot, matrikG, matrikM
import numpy as np


# Perhitungan Gravitasi
# =============================================================================
# Data
t = [0.00, 0.25, 0.50, 0.75,
     1.00, 1.25, 1.50, 1.75,
     2.00, 2.25, 2.50, 2.75,
     3.00, 3.25, 3.50, 3.75,
     4.00, 4.25, 4.50, 4.75,
     5.00]

h = [5.00, 5.75, 6.40, 6.94,
     7.38, 7.72, 7.96, 8.10,
     8.13, 8.07, 7.90, 7.62,
     7.25, 6.77, 6.20, 5.52,
     4.73, 3.85, 2.86, 1.77,
     0.58]

# Gambar
plot(t, h)

# matrix t2
index_h0 = t.index(0)
h0 = h[index_h0]
t2 = []
for i in range(len(t)):
    t2.append(t[i]**2)

# matrix G
G = matrikG([t, t2])

# matrix d
d = []
for i in range(len(h)):
    d.append(h[i] - h0)
d = np.array(d)

m = matrikM(G, d)
print("\nParameter yang di cari: \n", m)
g = -2*m[1]
print("\nNilai gravitasi yang diperoleh: \n", g)
