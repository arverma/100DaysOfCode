# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 21:53:37 2019

@author: amanranjan
"""

def spiral(n):
    a = [[ 0 for i in range(n)] for j in range(n)]
    l = 0
    t = 0
    b = n-1
    r =  n-1
    left = 1
    right = 0
    up = 0
    down = 0
    temp  = 1
    while(l <= r and t <= b):
        if(left):
            #print("left")
            for i in range(l, r+1):
                a[:][l][i] = temp
                temp += 1
                #print(a)
            left = 0
            down = 1
            t += 1
            pass
        elif(down):
            #print("down")
            for i in range(t, b+1):
                a[:][i][r] = temp
                temp += 1
                #print(a)
            down = 0
            right = 1
            r -= 1
            pass
        elif(right):
            #print("right")
            for i in range(r, l-1, -1):
                #print(b, i)
                a[:][b][i] = temp
                temp += 1
                #print(a)
            up = 1
            right = 0
            b -= 1
            pass
        elif(up):
            #print("up")
            for i in range(b, t-1 , -1):
                a[:][i][l] = temp
                temp += 1
                #print(a)
            up = 0
            left = 1
            l += 1
            pass
    return a

# =============================================================================
# def spiral(n):
#     
#     result = [[0 for i in range(n)] for j in range(n)]
#     coord = [[(i,j) for j in range(n)] for i in range(n)]
#     print(result)
#     print(coord)
#     
#     count = 1
#     
#     while coord:
#         for x, y in coord.pop(0):
#             print(x,y)
#             result[x][y] = count
#             count += 1
#         coord = list(zip(*coord))[::-1]
#         print(coord)
# 
#     return result
# 
# =============================================================================
n = 4
a = spiral(n)
print(a)