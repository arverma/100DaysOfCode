# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 12:46:40 2018

@author: amanranjan
"""

class stack():
    def __init__(self, a):
        self.a = a
        self.size = 0
    def isEmpty(self):
        if(self.size == 0):
            return True
        else:
            return False
    def isFull(self, n):
        if(self.size == n):
            return True
        else:
            return False
    def push(self, key):
        if(self.isFull(4) == False):
            self.a.append(key)
            self.size += 1
            return self.a
        else:
            return "Stack Full"
    def pop(self):
        if(self.isEmpty() == False):
            delete = self.a[self.size-1]
            self.a = self.a[0:self.size-1]
            self.size -= 1
            return [self.a, delete]
        else:
            return "Stack Empty"
    def peek(self):
        return self.a[self.size-1]

a = []
s = stack(a)
print(s.isEmpty())
print(s.pop())
print(s.push(5))
print(s.push(4))
print(s.push(1))
print(s.push(2))
print(s.push(3))
print(s.isFull(4)) #4 is max capacity
print(s.peek())
print(s.pop())