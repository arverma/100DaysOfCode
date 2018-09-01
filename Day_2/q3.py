# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 16:05:33 2018

@author: amanranjan
"""

n = int(input())
odd = 0
if(n%2 == 0):
    while(n>=2):
        odd = odd + n*n
        n = n-2
else:
    while(n>=1):
        odd = odd + n*n
        n = n-2
print(odd)
        