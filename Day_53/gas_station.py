# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 21:30:16 2019

@author: amanranjan
"""

# =============================================================================
# def canCompleteCircuit(A, B):
#     for i in range(len(A)):
#         store = 0
#         required = 0
#         count = 0
#         for j in range(i, len(A)+i):
#             store += A[j%len(A)]
#             required = B[j%len(A)]
#             if(store >= required):
#                 count += 1
#                 store -= required
#                 if(count == len(A)):
#                     return i
#             else:
#                 break
#     return -1
# =============================================================================

def canCompleteCircuit(A, B):
    circle = 0
    i = 0
    store = 0
    start = 0
    A = A + A
    B = B + B
    if(sum(A) < sum(B)):
        return -1
    else:
        while(circle != len(A)/2):
            store += A[i]
            if(store >= B[i]):
                store -= B[i]
                circle += 1
            else:
                store = 0
                circle = 0
                start = i+1
            print(i, start, circle, store)
            i += 1
        print(i,start, circle)
        return start
    
A = [6, 3, 7]
B = [4, 6, 3]
#A = [0]
#B = [0]
print(canCompleteCircuit(A, B))



# =============================================================================
# 
# def canCompleteCircuit(self, gas, cost):
#         if sum(gas) < sum(cost):
#             return -1
#         n = len(gas)
#         diff = 0
#         stationIndex = 0
#         for i in range(n):
#             if gas[i]+diff < cost[i]:
#                 stationIndex = i+1
#                 diff = 0
#             else:
#                 diff += gas[i]-cost[i]
#         return stationIndex
# =============================================================================
