# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 16:38:54 2018

@author: amanranjan
"""


def GCD(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
    
  
def P(m):
    ans = 1
    k = 1
    while k<=m:
        #print(k,m,"GCD = ", GCD(k,m))
        if GCD(k,m) == 1:
            ans *= k
        k += 1
    return ans % m

A = int(input())
ans = 0
i = 1
while(i<=A):
    ans += P(i)
    i +=1
print( ans % 1000000007)

