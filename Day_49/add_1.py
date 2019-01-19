# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 21:10:45 2019

@author: amanranjan
"""

def add_1(a):
    j = 0
    if(len(a)>1):
        while(a[j]==0):
            j += 1
        a = a[j:len(a)]
        
    i = len(a)-1
    while(a[i] + 1 > 9):
        a[i] = 0
        i -= 1
    if(i >= 0):
        a[i] += 1
    else:
        a = [1] + a
    return a


a = [0, 0, 0, 9]
print(add_1(a))
