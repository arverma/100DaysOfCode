# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 11:48:15 2018

Searching in Row wise and column wise sorted array
Complexity = O(n + m)

@author: amanranjan
"""

a = [[0,1,5,9,98],[2,14,20,21,99],[3,30,34,43,100],[4,31,35,44,101]]
index = [0, 0]

[print(i) for i in a]

key = 10

def find_index(a, key):
    i = 0
    n = len(a[0])-1
    j = n
    
    while(a[i][j] != key):
#        print(i,j, a[i][j])
        if(key > a[i][j]):
            i += 1
        elif(key < a[i][j]):
            j -= 1
        if(i+1 > n or j-1 < 0):
            return "Not Found"
    index[0] = i
    index[1] = j
    return index
        
print(find_index(a, key))
