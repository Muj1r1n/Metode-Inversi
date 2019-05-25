#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 10:17:53 2019

@author: mujirin|mujirin@ui.ac.id
"""
import matplotlib.pyplot as plt
import numpy as np
import datetime


def matrikG(list_data):
    '''
    Pembuatan matrik G
    G = [[ 0.    ,  0.    ],
         [ 0.25  ,  0.0625],
         [ 0.5   ,  0.25  ],
         [ 0.75  ,  0.5625],
         [ 1.    ,  1.    ],
         [ 1.25  ,  1.5625]]
    dari
    list_data = [[1, 1, 1], [2, 2, 2], ....]
    '''
    matrikG = np.array(list_data).transpose()
    return matrikG


def matrikM(G, d):
    '''
    Perhitungan matrix m
    G: Komponen
    d: Target
    G = [[ 0.    ,  0.    ],
         [ 0.25  ,  0.0625],
         [ 0.5   ,  0.25  ],
         [ 0.75  ,  0.5625],
         [ 1.    ,  1.    ],
         [ 1.25  ,  1.5625]]
    d = [[ 0.  ],
         [ 0.75],
         [ 1.4 ],
         [ 1.94],
         [ 2.38],
         [-4.42]])
    '''
    # matrix Gt: G transpose
    G = np.array(G)
    Gt = G.transpose()

    # Inverse Gt*G
    # =============================================================================
    invGtG = np.linalg.inv(np.matmul(Gt, G))

    # m
    # =============================================================================
    m = np.matmul(np.matmul(invGtG, Gt), d)
    m = list(m)
    return m


def plot(z, T, line='o', name='gambar'):
    fig, ax = plt.subplots()
    ax.plot(z, T, line)
    ax.set(xlabel='Kedalaman (m)', ylabel='Temperatur (m)',
           title='Kedalaman vs Temperatur')
    ax.grid()
    fig.savefig(name + str(datetime.datetime.now()) + ".png")
    plt.show()
    return None
