# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 21:36:57 2019

@author: amanranjan
"""

def reserve(arr, dep, k):
    events = [(t, 1) for t in arr] + [(t, 0) for t in dep]
    events = sorted(events)
    print(events)
    res = []
    for i in range(len(arr)):
        res.append([arr[i], dep[i]])
    res = sorted(res, key = lambda x:x[0])
    for i in range(len(res)-1):
        k -= 1
        if(res[i][1] >= res[i+1][0]):
            k -= 1
            if(k < 0):
                return False
        else:
            k += 1
        print(res[i][1], res[i][0], k)
    return True

arr = [1, 2, 3, 4]
dep = [10, 2, 6, 14]
k = 2

print(reserve(arr, dep, k))