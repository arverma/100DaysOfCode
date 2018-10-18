# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 14:35:53 2018

@author: amanranjan
"""

a = [2, 1, 5, 6, 3]
k = 3
end = len(a)-1
start = 0
count = 0
for i in range(len(a)):
    print(start, end, a)
    if(start > end):
        break
    if(a[start] > k and a[end] <=k ):
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1 
        count +=1
    elif( a[end] > k):
        end -= 1
    elif( a[start] < k):
        start += 1
print(count)
    