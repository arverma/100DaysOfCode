# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 13:44:25 2018

@author: amanranjan
"""

import random as r

a = [[10,8,10,10],[14,13,12,11],[15,9,11,21],[16,17,19,20]]
print(a[0][:],"\n",a[1][:],"\n",a[2][:],"\n",a[3][:])

j = r.randint(0,len(a[0])-1)
i = 0
print(i,j,a[i][j])

def GAA(a,i,j):
#    print(a[i][j])
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


