# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 21:53:43 2019

@author: amanranjan
"""

def duplicate(a):
    temp = {}
    for i in a:
        temp[i] = 1 + temp.get(i, 0)
    print(temp)
    for i in temp.keys():
        if(temp[i] > 1):
            return i
    return -1

a = [3, 4, 1, 4, 1]
print(duplicate(a))