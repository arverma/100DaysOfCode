# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 20:11:04 2019

@author: amanranjan
"""

def fact(n):
    if(n <= 0):
        return 1
    return n*fact(n-1)

def pascal(n):
    temp = []
    for j in range(1, n+2):
        temp.append(int(fact(n)/(fact((n)-j+1)*fact((j)-1))))
    return temp

print(pascal(0))
#when k = 3, the row is [1,3,3,1]