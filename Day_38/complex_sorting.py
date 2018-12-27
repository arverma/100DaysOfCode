# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 12:24:36 2018

[First Name, Last Name, age, children]

sort with first name
1. if 1st name is same, go with last name
2. if 1st name, last name are same, go with age
3. if 1st name, last name, age are same, go with children

@author: amanranjan
"""
employee = [["Aman", "Ranjan", 61, 2], ["Aman", "Ranjan", 16, 3], ["Human", "Verma", 31, 3], ["Aman", "Raj", 16, 1], ["Ranjan", "Verma", 26, 2], ["Aman", "Ranjan", 61, 1] ]

b = sorted(employee, key=lambda t: t[0])
for a in b:
    print(a)
#%%
for i in range(1,4):
    p = 0
    q = 0
    temp = ""
    for a in b:
        print(a[i-1], temp, end = " ")
        if(a[i-1]!=temp):
            b[p:q] = sorted(b[p:q], key=lambda t: t[i])
            print(",",p,q)
            p = q
            temp = a[i-1]
            for k in b:
                print(k)
        else:
            print(p,q)
        q += 1
#for a in b:
#    print(a)