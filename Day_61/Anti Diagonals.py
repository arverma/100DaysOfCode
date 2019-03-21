# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 21:56:27 2019

@author: amanranjan
"""

def diag(a):
    #print(a)
    res = []
    for i in range(len(a)):
        temp = []
        for j in range(i+1):
            temp.append(a[j][i-j])
        res.append(temp)
        temp = []
        #print(res)
    for i in range(1, len(a)):
        temp = []
        for j in range(len(a)-i):
            temp.append(a[j+i][len(a)-1-j])
        res.append(temp)
        temp = []
        #print(res)
    return res

a = [[1, 2, 3], [3, 6, 1], [9, 7, 8]]
print(diag(a))