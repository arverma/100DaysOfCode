# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 21:28:56 2018

@author: amanranjan
"""
a = "man"

# =============================================================================
# for i in range(len(a)):
#     print(a[len(a)-i-1], end ="")
# =============================================================================

def rev(a, start, end):
    if(start < end):
        a[start], a[end] = a[end], a[start]
        return rev(a, start+1, end-1)
    else:
        return a

print(rev(list(a), 0, len(a)-1))