# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 11:45:35 2018

@author: amanranjan
"""

a = [1, 2, 2, 1]
n = len(a)
a.sort()
b = []
b.extend(a)
j = 0
k = 0
for i in range(n):
    if(i%2 == 0):
        a[i] = b[n-j-1]
        j += 1
    else:
        a[i] = b[k]
        k +=1
print(a)