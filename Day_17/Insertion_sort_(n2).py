# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 11:07:29 2018

@author: amanranjan
"""

a = [-12, 11, 0, -5, 6, -7, 5, -3, -6]

for i in range(len(a)-1):
    if(a[i+1]<a[i]):
        print(a)
        j = i
        key = a[i+1]
        while(key<a[j]):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
print(a)