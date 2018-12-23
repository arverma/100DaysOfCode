# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 10:43:54 2018

@author: amanranjan
"""

#import random
import math as m
a = [12, 3, 5, 7, 4, 19, 26]
b = sorted(a)
k = 2

def medianOfMedian(a,b):
    median = []
    if(len(a) > 5):
        for i in range(0, m.floor(len(a)/5)):
            median.append(sorted(a[5*i:5*(i+1)])[2])
#            print(i, a[5*i:5*(i+1)], sorted(a[5*i:5*(i+1)]), median)
        return medianOfMedian(median,b)
    else:
        return b.index(sorted(a)[m.floor(len(a)/2)]) # Return index of the median

#print(medianOfMedian(a))
def kth_smallest(a, p, q, k):
#    r = random.randint(p, q-1)
    r = medianOfMedian(a[p:q],b)
    print(a,"p=",p,"q=",q,"r=",r)
    a[p], a[r] = a[r], a[p]
    index = p
    for i in range(p+1,q):
        print(a,r,index)
        if(a[i]<a[p]):
            index +=1
            a[index], a[i] = a[i], a[index]
    a[index], a[p] = a[p], a[index]
    
    if(k < index):
        return kth_smallest(a, p, index, k)
    elif(k > index):
        return kth_smallest(a, index+1, q, k)
    else:
        return a[index]

print("For K =",k," smallest = ",kth_smallest(a, 0, len(a), k), ", Check=", b[k])
