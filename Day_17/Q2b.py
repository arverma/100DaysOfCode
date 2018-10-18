# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 14:36:13 2018

@author: amanranjan
"""

def r_rotate(a,i,j,n):
    a = a[0:i] + [a[j]] + a[i:j] + a[j+1:n]
    return a
    #print(a)



a = [12, 11, -13, -5, 6, -7, 5, -3, -6]
n = len(a)
# r_rotate(a,0,2,n)

i = 0
for j in range(n):
    if(a[j] < 0):
        a = r_rotate(a,i,j,n)
        i+=1
    print(i,j,a)
    
