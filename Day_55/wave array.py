# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 21:25:55 2019

@author: amanranjan
"""

def wave(a):
    a.sort()
    for i in range(0,len(a),2):
        if(i < len(a)-1):
            a[i], a[i+1] = a[i+1], a[i]
    return(a)

a = [1, 2, 3, 4]
print(wave(a))