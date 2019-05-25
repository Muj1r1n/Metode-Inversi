#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 04:59:37 2019

@author: thomas
"""
import numpy as np
x = [2, 4, 6, 8]
t = [5.1, 9.2, 11.9, 14.9]

d = t
from inversi import matrikG, matrikM, plot

#m = [a0, a1]
one = np.ones(len(x))
G = matrikG([one, x])
m = matrikM(G, d)
print("a0(intercept): ", m[0])
print("a1(slope): ", m[1])

v = 1/m[1]
print("v: ", v)
plot(x,t)

# =============================================================================
# 
# =============================================================================
xdata = np.array([0.0,1.0,2.0,3.0,4.0,5.0])
ydata = np.array([0.1,0.9,2.2,2.8,3.9,5.1])
x0    = np.array([0.0, 0.0, 0.0])

sigma = np.array([1.0,1.0,1.0,1.0,1.0,1.0])

# model
def func(x, a, b, c):
    return a + b*x + c*x*x

import scipy.optimize as optimization

opt = list(optimization.curve_fit(func, xdata, ydata, x0, sigma))

m = list(opt[0])

print(m)


def func(params, xdata, ydata):
    return (ydata - np.dot(xdata, params))

xdata = np.transpose(np.array([[1.0,1.0,1.0,1.0,1.0,1.0],
              [0.0,1.0,2.0,3.0,4.0,5.0]]))
lq = optimization.leastsq(func, x0, args=(xdata, ydata))
print(lq)
