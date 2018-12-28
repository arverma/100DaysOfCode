# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 12:06:02 2018

@author: amanranjan
"""

import numpy as np
import math as m

a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#a = [3,4,5,6,7,18,29]
a = np.array(a)
key = 7

#[print(i) for i in a]
print(a)
#%%
def binary_search(a, start, end, key):
    mid = m.floor((start+end)/2)
#    print(a, mid)
    if( mid == len(a)-1):
        return mid
    else:
        if(a[mid] <= key and a[mid+1] > key ):
            return mid
        elif(a[mid] < key):
            return binary_search(a, mid+1, len(a)-1, key)
        elif(a[mid] > key):
            return binary_search(a, 0, mid-1, key)

def search(a, key):
    i = binary_search(a[:,0], 0, len(a[:,1])-1 , key)
    j = binary_search(a[i], 0, len(a[0])-1 , key)
    return [i+1,j+1]

print(search(a, key))