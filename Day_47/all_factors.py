# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 20:54:43 2019

@author: amanranjan
"""
import math as m

def factors(num):
    fact = set()
    for i in range(1, m.ceil(m.sqrt(num)+1)):
        if(num%i == 0):
            fact.add(i)
            fact.add(int(num/i))
    return fact


num = 17 #int(input())
print(sorted(factors(num)))
