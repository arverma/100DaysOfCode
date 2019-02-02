# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 20:54:51 2019

@author: amanranjan
"""

def nobel(a):
    a.sort() #[3,7,10,16]
    print(a)
    n = len(a)

    for i in range(n):
        if(a[i] == n-i-1 and a[i] != a[i+1]):
            return 1
    return -1

a = [ 1, 2, 7, 0, 9, 3, 6, 0, 6 ]
print(nobel(a))