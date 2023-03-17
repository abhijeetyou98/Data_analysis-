# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 11:03:20 2023

@author: AshwinSecond
"""

import numpy as np
import scipy.optimize as scopt
import matplotlib.pyplot as plt
import xlwings

wb = xlwings.Book("SecondOrderReaction.xlsx")


def get_row_col(cell):
    address = cell.address
    col, row = address.strip("$").split("$")
    row = int(row)
    return row, col

def get_data(startcell, nmax=10000):
    row, col = get_row_col(startcell)
    sheet = startcell.sheet
    data = sheet[f"{col}{row}:{col}{row+nmax}"].value
    data = np.array(data)
    booltype = data == None
    data = data[~booltype]
    return data

def model(t, Cstar, kLa, t0):
    u = -kLa*(t-t0)
    brac = np.e**u
    C = Cstar*(1-brac)
    boolnegative = C < 0.0
    C[boolnegative] = 0.0
    return C

def get_parameters(sheetname, paramguess, 
                   boolplot = True):
    sheet = wb.sheets(sheetname)
    
    tdata = get_data(sheet["B5"])
    Cdata = get_data(sheet["C5"])    
    
    Cstar, kLa, t0 = paramguess
    parameters = [Cstar, kLa, t0]
    p, covm = scopt.curve_fit(model, tdata, Cdata,
                              p0 = parameters)
    
    errp = np.diagonal(covm)**0.5

    if boolplot:
        Cstar, kLa, t0 = p
        Ccalc = model(tdata, Cstar, kLa, t0)
        plt.plot(tdata, Cdata, 'r.')
        plt.plot(tdata, Ccalc, 'b')
    return p, errp

paramguess = [8.0, 0.001, 100]
sheetnames = [sheet.name for sheet in wb.sheets if (sheet.name).startswith('n')]
parameter_matrix = []
for sheetname in sheetnames:
    p, errp = get_parameters(sheetname, paramguess, 
                             boolplot = False)
    entry = [float(sheetname.split('n')[-1])]+list(p) + list(errp)
    paramguess = p
    parameter_matrix.append(entry)
    
parameter_matrix = np.array(parameter_matrix)
sheet = wb.sheets("Output")
sheet["B5"].value = parameter_matrix

def check_fit(rpm):
    entry = [pm for pm in parameter_matrix if pm[0] == rpm][0]
    parameters = entry[1:4]
    sheetname = 'n'+str(int(rpm))
    p, errp = get_parameters(sheetname, parameters)
    entrynew = [rpm] + list(p) + list(errp)
    for i in range(len(entry)):
        e = entry[i]
        enew = entrynew[i]
        var = (enew - e)/enew * 100
        print(i, var)
    