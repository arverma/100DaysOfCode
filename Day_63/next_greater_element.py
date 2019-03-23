# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 17:43:04 2019

@author: amanranjan
"""

def nextgreater(a):
    stack = []
    stack.append(a.pop())
    res = [-1]
    #print(stack, res, a)
    while(len(a) != 0):
        while(len(stack)!= 0 and a[len(a)-1] >= stack[len(stack)-1]):
            stack.pop()
        if(len(stack) == 0):
            res.append(-1)
        else:
            res.append(stack[len(stack)-1])
        stack.append(a.pop())
        #print(stack, res, a)
    return [ res[i] for i in range(len(res)-1, -1, -1)]

a = [ 70, 80, 70, 38, 39,90]
print(nextgreater(a))