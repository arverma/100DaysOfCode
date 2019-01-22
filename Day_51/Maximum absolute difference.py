# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 22:30:38 2019

@author: amanranjan
"""

def max_abs(A):
    i = 0
    j = len(A)-1
    max1 = A[i]
    max2 = A[j]
    min1 = A[i]
    min2 = A[j]
    max1_i = 0
    max2_i = j
    min1_i = 0
    min2_i = j
    while(j>=i):
        if(A[i]-i>max1):
            max1 = A[i]
            max1_i = i
        if(A[i]+i<min1):
            min1 = A[i]
            min1_i = i
        if(A[j]-i>max2-i):
            max2 = A[j]
            max2_i = j
        if(A[j]+i<min2):
            min2 = A[j]
            min2_i = j
        print(max1,max2,min1,min2, i, j)
        i += 1
        j -= 1
    print(max1,max2,min1,min2)
    return max(abs(max1-min1)+abs(max1_i-min1_i), abs(max1-min2)+abs(max1_i-min2_i), abs(max2-min1)+abs(max2_i-min1_i), abs(max2-min2)+abs(max2_i-min2_i))

A = [ 53, 74, 34, 47, 47, 35, 86, 93, 91, 43]
print(max_abs(A))