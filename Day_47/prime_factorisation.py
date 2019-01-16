# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 22:38:45 2019

@author: amanranjan
"""

import math as m

def check_prime(a):
    for i in range(1, m.ceil(m.sqrt(a))+1):
        if(a%i == 0):
            return False
    return True

def prime_gen(a):
    p = [1]
    for i in range(2, a):
        if(check_prime(i)):
            p.append(i)
    return p

def factors(num, prime):
    fact = set()
    for i in prime:
        if(num%i == 0):
            fact.add(i)
    return fact

num = 17 #int(input())

prime = prime_gen(m.ceil(m.sqrt(num)))
print(factors(num, prime))