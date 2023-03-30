# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:23:42 2023

@author: AshwinSecond
"""
import numpy as np
import scipy.integrate as scint
import matplotlib.pyplot as plt

m_1 = 1
m_2 = 10
l_1 = 1
l_2 = 1
g = 9.81
sin = np.sin
cos = np.cos

def model(SV, t):
    
    [T_1, V_1, T_2, V_2] = SV
    
    dT_1bydt = V_1
    dT_2bydt = V_2
    
    Nr1 = 0.5*V_1**2*l_1**2*m_1*sin(2*T_1) + 0.25*V_1**2*l_1**2*m_2*sin(2*T_1) - 0.125*V_1**2*l_1**2*m_2*sin(2*T_1 - 2*T_2) - 0.125*V_1**2*l_1**2*m_2*sin(2*T_1 + 2*T_2) - 0.25*V_1**2*l_1*l_2*m_2*sin(2*T_1 - 2*T_2) + 0.25*V_1**2*l_1*l_2*m_2*sin(2*T_1 + 2*T_2) - 0.5*V_1**2*l_2**2*m_1*sin(2*T_1) - 0.25*V_1**2*l_2**2*m_2*sin(2*T_1) - 0.125*V_1**2*l_2**2*m_2*sin(2*T_1 - 2*T_2) - 0.125*V_1**2*l_2**2*m_2*sin(2*T_1 + 2*T_2) - 0.5*V_2**2*l_1*l_2*m_2*sin(T_1 - T_2) + 0.5*V_2**2*l_1*l_2*m_2*sin(T_1 + T_2) - 0.5*V_2**2*l_2**2*m_2*sin(T_1 - T_2) - 0.5*V_2**2*l_2**2*m_2*sin(T_1 + T_2) - 1.0*g*l_1*m_1*sin(T_1) - 1.0*g*l_1*m_2*sin(T_1) - 0.25*g*l_1*m_2*sin(T_1 - 2*T_2) + 0.25*g*l_1*m_2*sin(T_1 + 2*T_2) + 0.5*g*l_2*m_2*sin(T_1) - 0.25*g*l_2*m_2*sin(T_1 - 2*T_2) - 0.25*g*l_2*m_2*sin(T_1 + 2*T_2)
    Dr1 = -1.0*l_1**2*m_1*sin(T_1)**2 + 1.0*l_1**2*m_1 - 1.0*l_1**2*m_2*sin(T_1)**2*sin(T_2)**2 + 1.0*l_1**2*m_2*sin(T_2)**2 - 2.0*l_1*l_2*m_2*sin(T_1)*sin(T_2)*cos(T_1)*cos(T_2) + 1.0*l_2**2*m_1*sin(T_1)**2 - 1.0*l_2**2*m_2*sin(T_1)**2*sin(T_2)**2 + 1.0*l_2**2*m_2*sin(T_1)**2    
    
    Nr2 = -1.0*V_1**2*l_1**2*l_2*m_1*sin(T_2)*cos(T_1) - 1.0*V_1**2*l_1**2*l_2*m_2*sin(T_2)*cos(T_1) + 1.0*V_1**2*l_1*l_2**2*m_1*sin(T_1)*cos(T_2) + 1.0*V_1**2*l_1*l_2**2*m_2*sin(T_1)*cos(T_2) + 1.0*V_2**2*l_1**2*l_2*m_2*sin(T_1)**2*sin(T_2)*cos(T_2) - 1.0*V_2**2*l_1**2*l_2*m_2*sin(T_2)*cos(T_2) - 2.0*V_2**2*l_1*l_2**2*m_2*sin(T_1)*sin(T_2)**2*cos(T_1) + 1.0*V_2**2*l_1*l_2**2*m_2*sin(T_1)*cos(T_1) + 1.0*V_2**2*l_2**3*m_2*sin(T_1)**2*sin(T_2)*cos(T_2) + 1.0*g*l_1**2*m_1*sin(T_1)*cos(T_1 - T_2) - 1.0*g*l_1**2*m_1*sin(T_2) + 1.0*g*l_1**2*m_2*sin(T_1)*cos(T_1 - T_2) - 1.0*g*l_1**2*m_2*sin(T_2) + 1.0*g*l_1*l_2*m_1*sin(T_1)**2*sin(T_2) + 1.0*g*l_1*l_2*m_2*sin(T_1)**2*sin(T_2) - 1.0*g*l_2**2*m_1*sin(T_1)**2*sin(T_2) - 1.0*g*l_2**2*m_2*sin(T_1)**2*sin(T_2)
    Dr2 = l_2*(-1.0*l_1**2*m_1*sin(T_1)**2 + 1.0*l_1**2*m_1 - 1.0*l_1**2*m_2*sin(T_1)**2*sin(T_2)**2 + 1.0*l_1**2*m_2*sin(T_2)**2 - 2.0*l_1*l_2*m_2*sin(T_1)*sin(T_2)*cos(T_1)*cos(T_2) + 1.0*l_2**2*m_1*sin(T_1)**2 - 1.0*l_2**2*m_2*sin(T_1)**2*sin(T_2)**2 + 1.0*l_2**2*m_2*sin(T_1)**2)
    
    dV_1bydt = Nr1/Dr1
    dV_2bydt = Nr2/Dr2
    
    return [dT_1bydt, dV_1bydt, dT_2bydt, dV_2bydt]

SV0 = [np.pi, 0.0, np.pi, 0.0]
SV01 = [np.pi+1e-2,0, np.pi, 0.0]
t = np.linspace(0, 50, 1000)
solution = scint.odeint(model, SV0, t)
solution2 = scint.odeint(model, SV01, t)
theta1 = solution[:,0]
theta2 = solution[:,2]

theta12 = solution2[:,0]
theta22 = solution2[:,2]

def get_xy(t1, t2):
    x1 = l_1*sin(t1)
    x2 = x1 + l_2*sin(t2)
    y1 = -l_1*cos(t1)
    y2 = y1 - l_2*cos(t2)
    return x1, x2, y1, y2


fig = plt.figure(); ax = fig.add_subplot(111)
for i, tt in enumerate(t):
    t1 = theta1[i]
    t2 = theta2[i]
    x1, x2, y1, y2 = get_xy(t1, t2)
    t1 = theta12[i]
    t2 = theta22[i]
    x12, x22, y12, y22 = get_xy(t1, t2)
    ax.cla()
    ax.axis([-l_1-l_2, l_1+l_2, -l_1-l_2, l_1])
    ax.plot([0, x1, x2], [0, y1, y2], 'r')
    ax.scatter([0, x1, x2], [0, y1, y2])
    ax.plot([0, x12, x22], [0, y12, y22], 'b')
    ax.scatter([0, x12, x22], [0, y12, y22])

    plt.pause(0.0001)