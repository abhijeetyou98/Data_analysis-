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
sheet = wb.sheets("Consolidated")

def get_data(sheet, column):
    data = sheet[f"{column}1:{column}100000"].value
    data = np.array(data)
    data = data[data != None]
    return data

Tdata = get_data(sheet, "A")[2:].astype("float")
mgdata = get_data(sheet, "B")[2:].astype("float")
xdata = get_data(sheet, "C")[2:].astype("float")
ydata = get_data(sheet, "D")[2:].astype("float")

T = scintp.interp2d(xdata, mgdata, Tdata, kind='cubic')

fig = plt.figure()
aT = fig.add_subplot(211)

aT.plot(Tdata, T(xdata, mgdata), 'ro')
aT.plot([min(Tdata),max(Tdata)], [min(Tdata),max(Tdata)], 'k')
