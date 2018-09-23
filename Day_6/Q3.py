# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 15:24:59 2018

@author: amanranjan
"""

A= list(map(int, input (). split ()))
B= list(map(int, input (). split ()))
def dev(num):
    temp = 1
    for i in range(1, num + 1):
        if num % i == 0:
            temp = temp*i
    return temp
G = []
for j in range(0,len(A)):
    for k in range(j+1,len(A)+1):
        G.append(dev(max(A[j:k])))
        G.sort(reverse=True)

X = []
for l in B:
    X.append(G[l-1])