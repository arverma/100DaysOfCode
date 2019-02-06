# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 23:30:52 2019

@author: amanranjan
"""

def maxgap(a):
    a.sort()
    max_diff = 0
    diff = 0
    if(len(a) < 2):
        return 0
    for i in range(len(a)-1):
        diff = a[i+1] - a[i]
        if(diff > max_diff):
            max_diff = diff
    return max_diff

a = [2, 2, 2]
print(maxgap(a))