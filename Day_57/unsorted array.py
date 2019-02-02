# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 19:50:17 2019

@author: amanranjan
"""

def unsorted(a):
    x = sorted(a)
    p = -1
    q = -1
    for i in range(len(a)):
        if(a[i] != x[i]):
            p = i
            break
    for i in range(len(a)-1, 0, -1):
        if(a[i] != x[i]):
            q = i
            break
    return [p, q] if p!= -1 else -1 

a = [0, 1, 3]
print(unsorted(a))