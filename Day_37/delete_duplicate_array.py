# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:06:05 2018

@author: amanranjan
"""

a = [1,3,4,6,9,4,6,8,3,6,9,3,2,5,9,5,4,9,2,33,56,8]
unique = {}
for i in a:
    if(unique.get(i,0) == 0):
        unique[i] = 1
print(unique.keys())