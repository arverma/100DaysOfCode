# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 22:32:22 2019

@author: amanranjan
"""
def max_sum(a):
    res = []
    temp = []
    max_sum = a[0]
    for i in range(len(a)):
        if(a[i] >= 0):
            res.append(a[i])
        else:
            if(sum(res) >= max_sum):
                max_sum = sum(res)
                temp = res
            else:
                pass
            res = []
        print(temp, res)
    return temp if sum(temp) >= sum(res) else res


A = [ 0, 0, -1, 0 ]
print(max_sum(A))