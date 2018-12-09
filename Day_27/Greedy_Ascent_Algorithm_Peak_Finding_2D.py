# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 13:44:25 2018

@author: amanranjan
"""

import random as r

a = [[14,13,17],[15,16,9],[5,6,7]]
print(a[0][:],"\n",a[1][:],"\n",a[2][:])

j = r.randint(0,len(a[0])-1)
i = 0
print(i,j,a[i][j])

def GAA(a,i,j):
    if(i<len(a)-1 and a[i+1][j]>a[i][j]):
        return GAA(a,i+1,j)
    elif(i>0 and a[i-1][j]>a[i][j]):
        return GAA(a,i-1,j)
    elif(j<len(a)-1 and a[i][j+1]>a[i][j]):
        return GAA(a,i,j+1)
    elif( j>0 and a[i][j-1]>a[i][j]):
        return GAA(a,i,j-1)
    else:
        return a[i][j]

print("Peak = ", GAA(a,i,j))


