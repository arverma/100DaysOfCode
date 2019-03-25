# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 11:37:39 2019

@author: amanranjan
"""
def segregate(a):
    j = len(a)-1
    for i in range(j+1):
       # print(a)
        if(a[i] <= 0):
            while(j > i and a[j] <= 0):
                j -= 1
            a[i], a[j] = a[j], a[i]
    return a, j

def first_missing(a):
    if(1 not in a):
        return 1
    else:
        a, j = segregate(a)[0], segregate(a)[1]
        for i in a[0:j+1]:
            if(abs(i) - 1 < len(a) and a[abs(i)-1] > 0):
                a[abs(i)- 1] = -a[abs(i)-1]
                
        for i in range(len(a)):
            if(a[i] > 0):
                return i+1
        return i+2

a = [ 1, 2, 3, 4, 5, 6 ]
print(first_missing(a))