# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:24:23 2023

@author: AshwinSecond
"""

import numpy as np
import scipy.integrate as scint
import matplotlib.pyplot as plt

mu = 1
K  = 10
S0 = 10
X0 = 0.001
Y = 1

def model(SV, t):
    [X, S] = SV
    
    dXbydt = mu*S/(K+S)*X
    dSbydt = -1/Y*dXbydt
    
    return [dXbydt, dSbydt]

t = np.linspace(0, 50, 100)
solution = scint.odeint(model, [X0, S0], t)
X = solution[:,0]
S = solution[:,1]

plt.plot(t, X, 'r')
plt.plot(t, S, 'b')
    
    