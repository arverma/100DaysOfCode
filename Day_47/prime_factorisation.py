# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 22:38:45 2019

@author: amanranjan
"""

import math as m

def prime_factors(num):
    prime = set()
    i = 2
    count = 0
    while(num>1):
        if(num%i==0):
            prime.add(i)
            num = int(num/i)
        elif(num%i!=0 and i <= m.sqrt(num)):
            i += 1
        else:
            prime.add(num)
            num = 1
        count += 1
    return prime, count

num = 44
print(prime_factors(num))