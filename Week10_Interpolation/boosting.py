# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 14:38:11 2023

@author: AshwinSecond
"""

import numpy as np
import sklearn.ensemble as EN
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

df["integer"] = list(range(len(df)))
booltest = df["integer"] % 3 == 0 
dftrain = df[~booltest]
dftest  = df[booltest]

ytrain = np.array(dftrain["T"])
Xtrain = np.array(dftrain[["mg", "x"]])

ytest = np.array(dftest["T"])
Xtest = np.array(dftest[["mg", "x"]])

reg = EN.GradientBoostingRegressor(
    n_estimators = 20
    )
reg = reg.fit(Xtrain, ytrain)
trainscore = reg.score(Xtrain,ytrain)
testscore = reg.score(Xtest,ytest)

Tpred_train = reg.predict(Xtrain)
Tpred_test  = reg.predict(Xtest)

plt.plot(ytrain, Tpred_train, 'ro')
plt.plot(ytest,  Tpred_test , 'bo')
plt.plot([min(Tdata), max(Tdata)], [min(Tdata), max(Tdata)], 'k')


fig = plt.figure(); ax = fig.add_subplot(111)
listx = np.linspace(0,1,100)
listmg = [0.0, 0.2, 0.4, 0.6]
colors = ['r', 'b', 'g', 'y']
for i, mg in enumerate(listmg):
    listT = []
    for xx in listx:
        x = (1-mg)*xx
        T = reg.predict([[mg, x]])
        listT.append(T)
    ax.plot(listx, listT, colors[i], label=f"mg={mg}")
ax.legend()
