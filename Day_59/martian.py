# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:12:50 2019

@author: amanranjan
"""
import numpy as np
def martian(x,y):
    x = np.array(x)
    y = np.array(y)
    #print(x)
    #print(y)
    max_sum = 0
    i = len(x[0,:])-1
    j = len(x[:,0])-1
    while(i >= 0 and j >= 0):
        temp = max(sum(x[i, 0:j+1]), sum(y[0:i+1, j]))
        indx = [sum(x[i, 0:j+1]), sum(y[0:i+1, j])].index(temp)
        max_sum += temp
        if(indx == 0):
            #print(x[i, 0:j+1])
            i -= 1
        else:
            #print(y[0:i+1, j])
            j -= 1
        #print(max_sum)
    return max_sum


# =============================================================================
# n = 2*list(map(int,input().split()))[0]
# while(n != 0):
#     x = []
#     y = []
#     while( n > 0):
#         if(n > 4):
#             x.append(list(list(map(int,input().split()))))
#         else:
#             y.append(list(list(map(int,input().split()))))
#         n -= 1
#         
#     n = 2*list(map(int,input().split()))[0]
# =============================================================================
    
x = [[0, 0, 10, 9], [1, 3, 10, 0], [4, 2, 1, 3], [1, 1, 20, 0]]
y = [[10, 0, 0, 0], [1, 1, 1, 30], [0, 0, 5, 5], [5, 10, 10, 10]]
print(martian(x,y))