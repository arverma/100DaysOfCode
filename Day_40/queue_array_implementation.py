# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 12:44:00 2018

@author: amanranjan
"""


class queue():
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
    def enqueue(self, key):
        if(self.isFull(4) == False):
            self.a = [key] + self.a
            self.size += 1
        else:
            return "Queue FULL"
        return self.a
    def dequeue(self):
        if(self.isEmpty() != True):
            self.a = self.a[0:len(self.a)-1]
            self.size -= 1
        else:
            return "Queue Empty"
        return self.a

a = []
q = queue(a)
print(q.isEmpty())
print(q.dequeue())
print(q.enqueue(2))
print(q.enqueue(3))
print(q.enqueue(4))
print(q.enqueue(5))
print(q.enqueue(5))
print(q.isFull(4)) # 4 is max capacity
print(q.dequeue())
    