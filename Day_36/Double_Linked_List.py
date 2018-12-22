# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 12:06:45 2018

@author: amanranjan
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class double_ll:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, data):
#        print(self.size)
        curr_node = self.head
        if(self.size >= 1):
            while(curr_node.next != None):
                curr_node = curr_node.next
#            print(data)
            new_node = Node(data)
            curr_node.next = new_node
            new_node.prev = curr_node
        else:
            new_node = Node(data)
            self.head = new_node
        self.size += 1
    
    def traverse(self):
        a = []
        curr_node = self.head
        while(curr_node):
            a.append(curr_node.data)
            curr_node = curr_node.next
        print(a)
        
    def delete_duplicate(self):
        curr_node = self.head
        a = []
        while(curr_node):
#            print(a)
            if(curr_node.data in a):
               duplicate = curr_node
               curr_node = curr_node.prev
               curr_node.next = duplicate.next
               curr_node = curr_node.next
            else:
                a.append(curr_node.data)
                curr_node = curr_node.next
        
myList = double_ll()     
myList.append(16)
myList.append(16)
myList.append(12)
myList.append(38)
myList.append(12)
myList.append(22)
myList.append(22)
myList.traverse()
myList.delete_duplicate()
myList.traverse()