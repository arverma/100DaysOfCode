# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 21:54:18 2018

@author: amanranjan
"""
import math as ma
x = "1234567"
y = "0076543"

def mul(x,y):
    n = len(list(x))
    if(n>1):
        a = x[0:ma.floor(n/2)]
        b = x[ma.floor(n/2)::]
        c = y[0:ma.floor(n/2)]
        d = y[ma.floor(n/2)::]
        print(a,b,c,d)
        ac = mul(a,c)
        bd = mul(b,d)
        xy = pow(10,2*(n-ma.floor(n/2)))*ac + pow(10, n-ma.floor(n/2))*((int(a)+int(b))*(int(c)+int(d))-ac-bd) + bd
        return xy
    else:
        return int(x)*int(y)

print("Multiplication = ", mul(x,y))