# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 14:01:16 2018

@author: amanranjan

""" 
def is_prime(num):
    temp = 0
    for i in range(2, int(num/2)):
        if num % i  == 0:
            temp = 1
            break
    if(num == 1 ):
        temp = 1
    return temp

a= list(map(int, input (). split ()))
for j in range(0,len(a)):
    for k in range(j+1,len(a)+1):
        print(a[j:k],sum(a[j:k]), is_prime(sum(a[j:k])))
       


""" """ 