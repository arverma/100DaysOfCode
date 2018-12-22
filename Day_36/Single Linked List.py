# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 20:48:14 2018
1. Add first
2. Add Last
3. Add at kth Position
4. Delete First
5. Delete Last
6. Delete specific value
7. Traverse
@author: amanranjan
"""

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def add_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def append(self,data):
        curr_node = self.head
        while(curr_node.next!= None):
#            print("data",curr_node.data)
            curr_node = curr_node.next
        new_node = Node(data)
        curr_node.next = new_node
        self.size += 1
    
    def insert(self, data, index):
        curr_node = self.head
        if(index <= self.size):
            for i in range(index-1):
                curr_node = curr_node.next
#                print(curr_node.data)
            last_node = curr_node.next
            new_node = Node(data)
            curr_node.next = new_node
            new_node.next = last_node
            self.size += 1
  
    def delete_first(self):
        curr_node = self.head
        self.head = curr_node.next
        self.size -= 1
    
    def delete_last(self):
        curr_node = self.head
        while(curr_node.next.next != None):
            curr_node = curr_node.next
        curr_node.next = None
        self.size -= 1
    
    def delete(self, data):
        curr_node = self.head
        if(curr_node.data != data):
            while(curr_node.next.data != data):
                curr_node = curr_node.next
            curr_node.next = curr_node.next.next
        else:
            self.head = curr_node.next
        self.size -= 1
            
    def traverse(self):
        a= []
        curr_node = self.head
        while(curr_node != None):
            a.append(curr_node.data)
#            print(curr_node.data)
            curr_node = curr_node.next
        print(a, self.size)

myList = LinkedList()
myList.add_front(5)
myList.add_front(8)
myList.add_front(2)
myList.traverse()
myList.append(16)
myList.append(18)
myList.append(12)
myList.traverse()
myList.delete_first()
myList.traverse()
myList.delete_last()
myList.traverse()
myList.insert(9,3)
myList.traverse()
myList.delete(16)
myList.traverse()
#print("size="+str(myList.get_size()))
#print(myList.remove(12))
#print("size="+str(myList.get_size()))
#print(myList.find(5))