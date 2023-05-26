# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 14:38:11 2023

@author: AshwinSecond
"""

import numpy as np
import scipy.interpolate as scintp
import matplotlib.pyplot as plt
import xlwings
wb = xlwings.Book("HNO3-H2O-MgNO3-VLE.xlsx")
sheet = wb.sheets("Binary")

def get_data(sheet, column):
    data = sheet[f"{column}1:{column}100000"].value
    data = np.array(data)
    data = data[data != None]
    return data

Tdata = get_data(sheet, "A")[2:].astype("float")
xdata = get_data(sheet, "B")[2:].astype("float")
ydata = get_data(sheet, "C")[2:].astype("float")

fig = plt.figure(); 
aTbubble = fig.add_subplot(311)
ay = fig.add_subplot(312)
aTdew = fig.add_subplot(313)

aTbubble.plot(xdata, Tdata, 'bo')
aTdew.plot(ydata, Tdata, 'ro')
ay.plot(xdata, ydata, 'go')

Tbubble = scintp.UnivariateSpline(xdata, Tdata, k=3)
y = scintp.UnivariateSpline(xdata, ydata, k=3, s=0.01)


x = np.linspace(0,1,1000)
aTbubble.plot(x, Tbubble(x), 'b')
ay.plot(x, y(x), 'c')
aTdew.plot(y(x), Tbubble(x),'r')

