# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 16:00:12 2019

@author: amanranjan
"""
import numpy as np

def rotate(a):
    if(len(a) != 1):
        l = 0
        r = len(a[0]) -1
        t = 0
        b = len(a) -1
        print(l, r, t, b)
        while(r > l and b > t):
            for i in range(l, r):
                print(i, np.array(a), "\n")
                temp = a[l][i]
                a[l][i] = a[b-i][l]
                a[b-i][l] = a[b][r-i]
                a[b][r-i] = a[t+i][r]
                a[t+i][r] = temp
            r -= 1
            b -= 1
            l += 1
            t += 1
            print(l, r, t, b)
    else:
        return a
    return a

a = [[1, 2, 3, 4], [ 5, 6, 7, 8], [ 9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]] 
#a = [[1, 2], [3, 4]]
#print(np.array(a))
print(np.array(rotate(a)))