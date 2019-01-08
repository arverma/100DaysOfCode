# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 14:44:17 2018

@author: amanranjan
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
class BST():
    def __init__(self):
        self.root = None
        
    def insert(self, data, c_time):
        if(self.root):
            self._insert(self.root, data, c_time)
        else:
            self.root = Node(data)
    
    def _insert(self,  curr_node, data, c_time):
        if(data > c_time):
            if(data < curr_node.data):
                if(curr_node.left == None):
                    if(curr_node.data >= data+3):
                        curr_node.left = Node(data)
                    else:
                        print("Not empty", curr_node.data, "-", data, "< 3")
                else:
                    self._insert(curr_node.left, data, c_time)
            else:
                if(curr_node.right == None):
                    if(curr_node.data <= data+3):
                        curr_node.right = Node(data)
                    else:
                        print("Not empty", data, "-", curr_node.data, "< 3")
                else:
                    self._insert(curr_node.right, data, c_time)
        else:
            print("Time has passed for", data, ". Current time = ", c_time)

    def inorder(self):
        if(self.root):
            self._inorder(self.root)
    
    def _inorder(self, curr_node):
        if(curr_node):
            self._inorder(curr_node.left)
            print(curr_node.data, end=" ")
            self._inorder(curr_node.right)

#%%
t = BST()
a = [11,9,3,14,50]
current_time = 5

for i in a:
    t.insert(i, current_time)
    t.inorder()
    print()
    
    