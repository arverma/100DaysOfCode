# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 12:26:51 2018

@author: amanranjan

Defination if Peak (1 Dimentional):
    if a[i] falls in between: a[i] is said to be peak if a[i]>=a[i-1] and a[i]>=a[i+1]
    if a[i] falls on edges: a[0] is said to be peak if a[0]>=a[1] or a[n] >=a[n-1]
    
"""

import math as m
a = [3,1,1,1,1,1,1]
a.reverse()

#%%
# Complexity O(n)
 Complexity O(n)
def peak(a):
    for i in range(len(a)):
        print(i)
        if(i==0 and a[i+1] <= a[i]):
            return a[i]
        elif(i>0 and i==len(a)-1 and a[i-1] <= a[i]):
            return a[i]
        elif(a[i]>=a[i+1] and a[i]>=a[i-1]):
            return a[i]
#%%
# Complexity Log2(n)
def peak(a):
    n = m.floor(len(a)/2)
    if(a[n]<a[n+1] and len(a)>1):
        return peak(a[n:len(a)])
    elif(a[n]<a[n-1] and len(a)>1):
        return peak(a[0:n])
    else:
        return a[n]
        
print("\n Peak = ",peak(a))