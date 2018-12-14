# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 15:36:30 2018

@author: amanranjan
"""
import math as m
#a = [16,14,10,8,7,9,3,2,4,1,0]
#a.reverse()

a = [0,2,4,1] # '0' is a dummy value just to make 1 indexing

print(a)

def build(a):
    for i in range(m.floor(len(a)/2), 0, -1):
        a = max_hepify(a,i)
#        print(a)
    return a

def max_hepify(a, i):
#    print(i, a[i])
    if((2*i <= len(a)-1 and a[i] < a[2*i]) or (2*i+1 <= len(a)-1 and a[i]<a[2*i +1])):
        if(2*i+1 > len(a)-1):
            a[i], a[2*i] = a[2*i], a[i]
            return max_hepify(a, 2*i)
        elif(a[2*i] < a[2*i +1]):
            a[i], a[2*i + 1] = a[2*i + 1], a[i]
            return max_hepify(a, 2*i+1)
        elif(a[2*i] > a[2*i +1]):
            a[i], a[2*i] = a[2*i], a[i]
            return max_hepify(a, 2*i)
    else:
        return a

def heap_sort(a):
    a = build(a)
#    print(a)
    for i in range(1,len(a)):
        a[1], a[len(a)-1] = a[len(a)-1], a[1]
        print(a.pop())
        a = build(a)
heap_sort(a)