# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 15:17:46 2019

@author: amanranjan
"""
import numpy as np

def zeros(a):
    row = []
    column = []
    for i in range(len(a)):
        if 0 in a[i]:
            row.append(i)
            
    if(len(row) != len(a)):
        for i in range(len(a[0])):
            if 0 in a[:,i]:
                column.append(i)
    print(row,column)
    
    for i in row:
        a[i] = [0 for i in a[0]]

    for i in column:
        a[:, i] = [0 for i in a[:,0]]
    return a

a = [
  [0,0,0],
  [1,1,0],
  [1,1,0]]
a = np.array(a)
print(zeros(a))