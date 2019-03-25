# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 17:02:53 2019

@author: amanranjan
"""
import numpy as np
import math as m
def rotate(a):
    if(len(a) != 1):
        t = 0
        b = len(a)-1
        # Mirror
        for i in range(m.floor(len(a)/2)):
            for j in range(len(a[0])):
                a[t][j], a[b][j] = a[b][j], a[t][j]
            t += 1
            b -= 1
        print(a, "\n")
        # Transpose
        for i in range(len(a)):
            j = 0
            while(j < i+1):
                a[i][j], a[j][i] = a[j][i], a[i][j]
                j += 1
            print(a, i)
    else:
        return a
    return a


a = [[1, 2, 3, 4], [ 5, 6, 7, 8], [ 9, 10, 11, 12], [13, 14, 15, 16]] 
#a = [[1, 2], [3, 4]]
print(np.array(rotate(np.array(a))))