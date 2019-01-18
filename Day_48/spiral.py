# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 16:35:18 2019

@author: amanranjan
"""

def spiralOrder( A):
    s = []
    m = len(A)
    n = len(A[0])
    
    t=0
    b=m-1
    l=0
    r=n-1
    
    dir = 0
    
    while( t<=b and l<=r):
        if(dir == 0):
            for i in range(l,r+1):
                s.append(A[t][i])
            t += 1
            dir = 1
        elif(dir == 1):
            for i in range(t,b+1):
                s.append(A[i][r])
            r -= 1
            dir = 2
        elif(dir == 2):
            for i in range(r,l-1,-1):
                s.append(A[b][i])
            b -= 1
            dir = 3
        else:
            for i in range(b,t-1,-1):
                s.append(A[i][l])
            l += 1
            dir = 0
    return s

print(spiralOrder([[1,2],[3,4],[5,6]]))