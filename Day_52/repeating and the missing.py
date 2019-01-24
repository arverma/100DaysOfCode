# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 22:05:09 2019

@author: amanranjan
"""

def repeat(a):
    twice = 0
    missing = 0
    j = 0
    for i in a:#range(len(a)):
        if(a[abs(i)-1] < 0):
            twice = abs(i)
        else:
            a[abs(i)-1] = -a[abs(i)-1]
        j += 1
    for i in range(len(a)):
        if(a[i] > 0):
            missing = i+1
    return [twice, missing]

a = [ 4, 3, 6, 2, 1, 1]
print(a)
print(repeat(a))