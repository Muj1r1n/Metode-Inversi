#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 10:17:53 2019

@author: mujirin|mujirin@ui.ac.id
"""
import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# Metode inversi garis
# =============================================================================
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

fig, ax = plt.subplots()
ax.plot(t, h, 'o')

ax.set(xlabel='Waktu (dt)', ylabel='Ketinggian (m)',
       title='waktu vs ketinggian')
ax.grid()

fig.savefig("test.png")
plt.show()


def inversiID(t, h):
    '''
    Calculating m1 + m2x
    '''
    index_h0 = t.index(0)
    h0 = h[index_h0]
    t2 = []
    for i in range(len(t)):
        t2.append(t[i]**2)

    # matrix G
    # =============================================================================
    G = np.array([t, t2]).transpose()
    # matrix Gt: G transpose
    Gt = G.transpose()

    # Gt*G
    # =============================================================================
    # GtG = np.matmul(Gt, G)

    # matrix d
    # =============================================================================
    d = []
    for i in range(len(h)):
        d.append([h[i] - h0])
    d = np.array(d)

    # Gtd
    # =============================================================================
    # Gtd = np.matmul(Gt, d)

    # Inverse Gt*G
    # =============================================================================
    invGtG = np.linalg.inv(np.matmul(Gt, G))

    # m
    # =============================================================================
    m = np.matmul(np.matmul(invGtG, Gt), d)
    return m


# =============================================================================
# g = 1.63364764 m/det^2
# =============================================================================
m = inversiID(t, h)
g = -2*m[1][0]
print("matrix m: \n", m)
print("g: \n", g)
