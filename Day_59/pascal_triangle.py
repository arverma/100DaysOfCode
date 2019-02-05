# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 19:40:34 2019

@author: amanranjan
"""

def fact(n):
    if(n <= 0):
        return 1
    return n*fact(n-1)

def pascal(n):
    trig = []
    for i in range(0, n+1):
        temp = []
        for j in range(1, i+2):
            temp.append(int(fact(i)/(fact(i-j+1)*fact(j-1))))
        trig.append(temp)
        temp = []
    return trig


print(pascal(0))