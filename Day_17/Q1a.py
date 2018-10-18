# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 14:34:53 2018

@author: amanranjan
"""

def minSwap(array, n, k):
    i = -1
    swaps = 0
    
    for j in range(0, n):
        if array[j] <= k:
            i += 1
            if i != j:
                swaps += 1
        print(j,i,swaps)

    return swaps

arr = [2, 1, 5, 6, 3] 
n = len(arr) 
k = 3
print (minSwap(arr, n, k)) 
  
arr1 = [2, 7, 9, 5, 8, 7, 4] 
n = len(arr1) 
k = 5
print (minSwap(arr1, n, k)) 