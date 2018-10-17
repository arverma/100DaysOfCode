# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 09:03:05 2018

@author: amanranjan
"""

arr = [1, 0, 9, 8, 0, 0, 4, 0, 2, 7, 6, 9]
print(arr)
n = len(arr)
count = 0
# index = -1
# for i in range(len(a)):
#     if(a[i]==0 and a[i-1]!=0):
#         index = i 
#     if(index != -1 and a[i]!=0):
#         a[index],a[i] = a[i], a[index]
#         index += 1
#         print(a)
for i in range(0, n): 
        if (arr[i] != 0): 
            arr[count], arr[i] = arr[i], arr[count] 
            count+=1
            print(arr)