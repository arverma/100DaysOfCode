# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:57:10 2018

@author: amanranjan
"""

def r_rotate(a,i,j,n):
    if(i!=0):
        a = a[0:i] + [a[j]] + a[i:j] + a[j+1:n]
    else:
        a = [a[j]] + a[i:j] + a[j+1:n]
    return a
    #print(a)

def f_index(a, start, end, k):
    mid = (start + end)//2
    # print(start, mid, end)
    # # print(a)
    # print([a[start]], [a[mid]], [a[end-1]])
    if(mid == 0):
        return 0
    elif(mid == start or mid == end-1):
        return mid + 1
    else:
        if(a[mid] > k):
            return f_index(a, 0, mid,  k)
        else:
            return f_index(a, mid, end, k)

a = [12, 11, 13, 5, 6]
# print(f_index(a[0:3], 5))
n = len(a)

i = 0
for j in range(n-1):
    if(a[j+1]<a[j]):
        start = 0
        end = len(a[0:j+1])
        index = f_index(a[0:j+1],start,end,a[j+1])
        print(index)
        a = r_rotate(a,index,j+1,n)
        print(a)
        
    
