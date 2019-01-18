# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 21:40:51 2019

@author: amanranjan
"""


def min_step(a, b):
    n = len(a)
    step = 0
    for i in range(n-1):#n-1
        c_x = a[i]
        c_y = b[i]
        n_x = a[i+1]
        n_y = b[i+1]
        print(c_x,c_y,step)
        step = step + max(abs(n_y - c_y), abs(n_x - c_x))
    return step


a = [  4, 1, 4, 10]
b = [ 6, 2, 5, 12 ]
print(min_step(a,b))