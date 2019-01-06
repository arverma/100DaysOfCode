# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 18:43:31 2019

@author: amanranjan
"""



def rec(p, count):
    if(p==1):
        count += 1
    elif(p==2):
        return 0
    
    for i in range(4):
        print(i, count)
        rec(p+1, count)

count = 1
rec(0, count)