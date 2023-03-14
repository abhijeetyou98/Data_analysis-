# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 11:03:20 2023

@author: AshwinSecond
"""

dcheros = ['batman','superman','flash','wonderwoman']
list_of_powers = ["none","flight","speed","strength"]
marvelheros = ['ironman','aquaman','hulk','blackwidow']
ordinarypeople = ['brucewayne','clarkkent','wallywest','dianaprince']



for hero in dcheros + marvelheros+ordinarypeople:
    if hero in dcheros:
        print(hero + " rocks")
    elif hero in marvelheros:
        print(hero + ' sucks')
    else:
        print(hero + ' who?')
        
herosdc = {
    "batman":{
        "power":"smarts",
        "ride":"batmobile",
        },
    "superman":{
        "power":["flight","strength","heatray","Xrayvision"],
        },
    "flash":{
        "power":"speed",
        "ride":"bus"
        },
    "wonderwoman":{
        "power":["strength","lasso"],
        "ride":"limousine"
        },
    }
    
        