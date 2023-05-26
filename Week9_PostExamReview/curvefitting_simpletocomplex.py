# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 09:33:22 2023

@author: AshwinSecond
"""

import numpy as np
import scipy.optimize as scopt
import matplotlib.pyplot as plt

def randompolynomial(x):
    y = x**2 + 5*x + 6
    return y

roots = np.roots([1,5,6])

#NEWTONS METHOD
listguess = np.linspace(-5,0,100)
listroot = []
for guess in listguess:
    root = scopt.newton(randompolynomial, guess)
    listroot.append(root)
#plt.plot(listguess, listroot, 'r')

def simeqn(params):
    [x,  y] = params
    resx = x**2 + y**2 - 16
    resy = 2*x + 3*y 
    return [resx, resy]

#LEAST-SQUARES METHOD
# plsq = scopt.least_squares(simeqn, [0.0, 1.0])

# colours = 10*['r','b','g','y','k','m']
# icol = 0
# listx = np.linspace(-5,5,10)
# listy = np.linspace(-5,5,10)
# list_solutions = []
# for x in listx:
#     for y in listy:
#         plsq = scopt.least_squares(simeqn, [x, y])
#         solution = np.array(plsq.x)
#         boolfound = False
#         i = 0
#         for i, sol in enumerate(list_solutions):
#             diff = np.array(solution) - np.array(sol)
#             if np.linalg.norm(diff) < 1e-6:
#                 boolfound = True
#                 break
#         if not boolfound:
#             index = i+1
#             list_solutions.append(solution)
#         else:
#             index = i
#         plt.plot(x, y, colours[index]+'o')
#         plt.pause(0.001)

#CURVE FITTING
#CAPTURE IN PANDAS DIRECTLY
import pandas as pd
# df = pd.read_excel("Data.xlsx",sheet_name="CpData")
# CAPTURE USING xlwings
def getData(sheet, column):
    data = sheet[f"{column}1:{column}100000"].value
    header = data[0]
    data = np.array(data[1:])
    data = data[data != None]
    return header, data
import xlwings
wb = xlwings.Book("Data.xlsx")
sheet = wb.sheets("CpData")
Theader, dataT = getData(sheet, "A")
Sheader, dataS = getData(sheet, "B")
df = pd.DataFrame({
    Theader:dataT,
    Sheader:dataS
    })

def S(T, parameters):
    [C1, C2, C3, C4, C5] = parameters
    
    S = C1
    S += C2 * ((C3/T)/np.sinh(C3/T))**2
    S += C4 * ((C5/T)/np.cosh(C5/T))**2
    return S

def Scalc(row, parameters):
    T = row["T"]
    Scalc = S(T, parameters)
    return Scalc

def residuals(parameters, df, ax):
    ax.cla()
    df["Scalc"] = df.apply(Scalc, axis=1, args=(parameters,))
    ax.plot(df["T"], df["S"], 'ro')
    ax.plot(df["T"], df["Scalc"], 'b')
    plt.pause(0.001)
    err = list(df["S"] - df["Scalc"])
    return err

fig = plt.figure(); ax = fig.add_subplot(111)
plsq = scopt.least_squares(residuals, [0,1,1,1,1],
                           args = (df, ax,))  
    
