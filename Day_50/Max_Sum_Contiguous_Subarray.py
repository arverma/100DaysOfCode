# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 21:29:58 2019

@author: amanranjan
"""

def subArray(a):
    max_i = 0
    ans = a[0]
    for i in range(len(a)):
        max_i = max(max_i+a[i],a[i])
        if(max_i > ans):
            ans = max_i
    return ans


a = [-2, -3, -1]
print(subArray(a))
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(subArray(a))