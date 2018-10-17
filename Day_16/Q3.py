# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 09:03:15 2018

@author: amanranjan
"""

a = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
#print(len(a))
j = 0
for i in range(len(a)):
    if(a[i]!=0):
        a[j] = a[i]
        j +=1
        #print("i",a, j)
for k in range(j,len(a)):
        a[k] = 0
print(a)