# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 21:00:34 2019

@author: amanranjan
"""
import math as m

def mejo(a):
    temp = {}
    mejority = 0
    for i in a:
        temp[i] = 1 + temp.get(i, 0)
    print(temp.keys())
    for i in list(temp.keys()):
        if(temp[i] > m.floor(len(a)/2)):
            mejority = i
    return mejority

a = [2]
print(mejo(a))