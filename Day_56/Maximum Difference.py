# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 22:11:36 2019

@author: amanranjan
"""

def max_diff(a): # j - i and j > i
    max_diff = 0
    diff = 0
    for i in range(len(a)-1, -1, -1):
        diff = max(diff, a[i]);
        max_diff = max(max_diff, diff-a[i]);
        print(max_diff, diff)
    return max_diff if max_diff > 0 else -1

def max_dff(a): # i - j and j > i
    max_diff = 0
    diff = 0
    for i in range(len(a)):
        diff = max(diff, a[i]);
        max_diff = max(max_diff, diff - a[i]);
        print(max_diff, diff)
    return max_diff if max_diff > 0 else -1

a = [3,0,2,1, 9]
print(max_dff(a))