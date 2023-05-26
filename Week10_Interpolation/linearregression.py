# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 14:38:11 2023

@author: AshwinSecond
"""

import numpy as np
import sklearn.linear_model as LM
import pandas as pd
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

df = pd.DataFrame({
    "T":Tdata,
    "mg":mgdata,
    "x":xdata,
    "y":ydata
    })

df["x2"] = df["x"]**2
df["mg2"] = df["mg"]**2
df["mgx"] = df["mg"]*df["x"]
df["x3"] = df["x"]**3
df["mg3"] = df["mg"]**3
df["mg2x"] = df["mg2"]*df["x"]
df["mgx2"] = df["mg"]*df["x2"]

y = np.array(df["T"])
X = np.array(df[["mg", "x", "x2", "mg2", "mgx", "x3","mg3","mg2x","mgx2"]])

reg = LM.LinearRegression()
reg = reg.fit(X, y)
score = reg.score(X,y)

Tpred = reg.predict(X)

plt.plot(df["T"], Tpred, 'ro')
plt.plot([min(Tdata), max(Tdata)], [min(Tdata), max(Tdata)], 'k')

fig = plt.figure(); ax = fig.add_subplot(111)
listx = np.linspace(0,1,100)
listmg = [0.0, 0.2, 0.4, 0.6]
colors = ['r', 'b', 'g', 'y']
for i, mg in enumerate(listmg):
    listT = []
    for xx in listx:
        x = (1-mg)*xx
        T = reg.predict([[mg, x, x**2, mg**2, mg*x, x**3, mg**3, mg**2*x, mg*x**2]])
        listT.append(T)
    ax.plot(listx, listT, colors[i], label=f"mg={mg}")
ax.legend()

