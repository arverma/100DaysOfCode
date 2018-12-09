# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 21:00:11 2018

@author: amanranjan

# =============================================================================
# Method: Divide and Conquer 
# =============================================================================
"""
import math as m
import numpy as np

a = np.asarray([[10,8,10,10],[14,13,12,11],[15,9,11,21],[16,17,19,20]])
#print(a[0][:],"\n",a[1][:],"\n",a[2][:],"\n",a[3][:])

def Peak2D(a):
    j = m.floor(len(a[0])/2)
    i = np.argmax(a[:,j])
    print(a)
    print(i,j,a[i,j])
    if(j<len(a[0])-1 and a[i][j+1]>a[i][j]):
        return Peak2D(a[:, j+1:len(a[0])])
    elif(j>0 and a[i][j-1]>a[i][j]):
        return Peak2D(a[:, 0:j])
    else:
        return a[i][j]

print("Peak = ", Peak2D(a))

