# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 19:24:21 2019

@author: amanranjan
"""

# =============================================================================
# def merge(array, x):
#     x = tuple(sorted(x))
#     result = []
#     temp = [0, 0]
#     flag = 1
#     if(x[1] < array[0][0]):
#         result.append(x)
#         [result.append(i) for i in array]
#         return result
#     
#     for a in array:
#         if(x[0] < a[1]):
#             if(flag == 1):
#                 temp[0] = min(a[0], x[0])
#                 if(x[1] < a[0]):
#                     temp[1] = x[1]
#                     result.append(tuple(temp))
#                     result.append(a)
#                 elif(x[1] < a[1]):
#                     temp[1] = max(x[1], a[1])
#                     result.append(tuple(temp))
#                 flag = 0
#             else:
#                 if(x[1] < a[1]):
#                     temp[1] = a[1]
#                     result.append(tuple(temp))
#                 elif(x[1] == a[0]):
#                     temp[1] = a[1]
#                     result.append(temp)
#         else:
#             result.append(a)
#         print(temp)
#     if(flag != 0):
#         result.append(x)
#     return result
# =============================================================================
# =============================================================================
# def merge(a, x):
#     x = tuple(sorted(x))
#     result = []
#     temp = [0, 0]
#     if(x[1] < a[0][0]):
#         result.append(x)
#         [result.append(i) for i in a]
#     elif(x[0] > a[len(a)-1][1]):
#         result = a
#         result.append(x)
#     else:
#         i = 0
#         while(x[0] > a[i][1]):
#             print(i)
#             result.append(a[i])
#             i += 1
#             
#         if(x[1] < a[i][1]):
#             temp[0] = min(x[0], a[i][0])
#             while(i < len(a) and x[1] < a[i][1]):
#                 if(x[1] < a[i][0]):
#                     temp[1] = min(x[1], a[i][0])
#                 else:
#                     temp[1] = max(x[1], a[i][1])
#                 i += 1
#                 print(temp)
#         else:
#             temp[0] = min(x[0], a[i+1][0])
#             while(i < len(a) and x[1] < a[i][1]):
#                 if(x[1] < a[i][0]):
#                     temp[1] = min(x[1], a[i][0])
#                 else:
#                     temp[1] = max(x[1], a[i][1])
#                 i += 1
#                 print(temp)
#             temp[1] = max(x[1], a[i][1])
#     return result
# =============================================================================
#print(temp, a[i][1], x[1])

def merge(a, x):
    x = tuple(sorted(x))
    a.append(x)
    a = sorted(a, key=lambda x: x[0])
    print(a)
    res = []
    temp = [0, 0]
    
    i = 0
    while(i < len(a)-1 and a[i][1] < a[i+1][0]):
        res.append(a[i])
        print(i)
        i+=1
        if(i == len(a)-1):
            res.append(a[i])
            return res
    temp[0] = a[i][0]
    tem = max(a[i][1], a[i+1][1]) 
    while(i < len(a)-1 and tem >= a[i+1][0]):
        i += 1
    temp[1] = max(a[i][1], tem)
    res.append(tuple(temp))
    print(i, temp)
    i += 1
    while(i < len(a)):
        res.append(a[i])
        i+=1
    return res

a = [(7, 8), (8,10), (18, 34), (45, 300)]
x =  (1, 3)
print(merge(a, x))




























