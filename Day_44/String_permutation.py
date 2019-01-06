# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 11:59:51 2019

@author: amanranjan
"""
def toString(a):
    return ["".join(a)]

def permute(a, l, j):
    if(l==j):
#        count += 1
        print(toString(a), end = " ")
#        print(x, count)
    else:
        for i in range(l, j+1):
            a[i], a[l] = a[l], a[i]
            permute(a, l+1, j)
#            print("me")
            a[i], a[l] = a[l], a[i]
#    return [x, count]
        
a = list("ABCD")
#count = 0
#print(permute(a, 0, len(a)-1, x, count))
permute(a, 0, len(a)-1)