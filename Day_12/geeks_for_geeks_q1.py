# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 17:17:27 2018

@author: amanranjan
"""

"""
#Time Complexity = O(d*n) Space Complexity = O(2)
"""
def rotate(a,d,n):
    temp = a[0:d]
    [a.remove(a[0]) for j in range(2)]
    a += temp
    return a

a = [1,2,3,4,5,6,7]
[print( ele, end = " ") for ele in rotate(a, 2, len(a))]

"""
#Time Complexity = O(d*n) Space Complexity = O(1)
"""

def rotate(a,d,n):
    for i in range(d):
        temp = a[0]
        a.remove(temp)
        a.append(temp)
    return a

a = [1,2,3,4,5,6,7]
[print( ele, end = " ") for ele in rotate(a,2,len(a))]

"""
#Time Complexity = O(n) Space Complexity = O(1)
#A Juggling Algorithm
"""

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)


def rotate(a,d,n):
    for i in range(gcd(d,n)):
        temp =  a[i]
        j=i
        while(i!=(j+d)%n):
            a[j] = a[(j+d)%n]
            j = (j+d)%n  
        a[j] = temp
    return a

a = [1,2,3,4,5,6,7]
[print( ele, end = " ") for ele in rotate(a,2,len(a))]
#print(gcd(3,len(a)))
