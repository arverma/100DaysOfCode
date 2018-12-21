# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 10:52:03 2018

@author: amanranjan
"""
import random
a = [3,6,1,8,9,5]
#a = [1,3,5,6,8,9]
k = 1

def quick_select(a,p,q,i):
    pass

def kth_smallest(a, p, q, k):
    r = random.randint(p, q-1)
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

print("K =",k,"smallest = ",kth_smallest(a, 0, len(a), k))