# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 10:37:06 2018

@author: amanranjan
"""
import math as m

a = [0,0,0,0,0,0,3,2,8,11,10,15,22]

def find_zeros(a, start, end):
    mid= m.floor((start+end)/2)
    print(start, mid, end)
    if(a[end] == 0):
        return end+1
    else:
        if(a[mid] != 0 and a[mid-1] == 0):
            return mid
        elif(a[mid] != 0):
            return find_zeros(a, 0, mid-1)
        elif(a[mid] == 0):
            return find_zeros(a, mid+1, len(a)-1)

print(find_zeros(a,0,len(a)-1))