# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 20:29:52 2018
@author: amanranjan

A sequence, a = [1, 10, 15, 26, 35, 32, 12], is called bitonic if it has a peak. Here '35'

"""
import math as m 

def bitonic(a, start, end):
    mid = m.floor((start+end)/2)
    if(mid != start or mid != end):
        if(a[mid] > a[mid-1] and a[mid] > a[mid+1]):
            return a[mid]
        elif(a[mid] > a[mid-1] and a[mid] <a[mid+1]):
            return bitonic(a, mid+1, end)
        elif(a[mid] < a[mid-1] and a[mid] > a[mid+1]):
            return bitonic(a, start, mid-1)
        pass
    else:
        return a[mid]

a = [1, 10, 15, 26, 35, 32, 12]
print(bitonic(a, 0, len(a)-1))