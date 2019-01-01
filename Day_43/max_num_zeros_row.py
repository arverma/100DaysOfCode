# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 21:03:28 2019

@author: amanranjan
"""
import math as m

def num_zeros(x, p, q, n):
    mid = m.floor((p+q)/2)
    if(mid<n and mid >= 0):
        if(x[mid] == 1 and x[mid+1] == 0):
            return n-mid
        elif(x[mid] == 1):
            return num_zeros(x, mid+1, q, n)
        elif(x[mid] == 0):
            return num_zeros(x, p, mid-1, n)
    else:
        return n-mid



a = [[1, 0, 0, 0, 0], [1, 1, 1, 0, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 1, 0, 0, 0]]

[print(i) for i in a]

max_ = 0
index = 0
n = len(a[0]) - 1

for i in range(len(a[0])):
    temp = num_zeros(a[i], 0, n, n)
#    print(max_ ,temp)
    if(temp > max_):
        max_ = temp
        index = i

print("At index", index, "Num of zeros = ", max_)
