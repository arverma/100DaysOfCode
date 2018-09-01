# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 15:45:10 2018

@author: amanranjan
"""

q = int(input())
i = 0
check = ['s','e','n','a','p','a','t','i','m','a','n','i','p','u','r']
while(i< q):
    i +=1
    s = input()
    j = 0
    flag = 1
    for chec in check:
        index = s.find(chec)
        if(index!= -1):
            s = s[index+1::]
        else:
            flag = 0
            break
    if(flag == 1 ):
        print("Good")
    else:
        print("Bad")