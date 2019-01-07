# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 20:46:06 2019

@author: amanranjan
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
class tree():
    def __init__(self):
        self.root = None
        
    def insert_level(self, data):
        if(self.root):
            self._insert(self.root, data)
        else:
            newNode = Node(data)
            self.root = newNode
            
    def _insert(self, curr_node, data):
        if(data < curr_node.data):
            if(curr_node.left == None):
                curr_node.left = Node(data)
            else:
                self._insert(curr_node.left, data)
        else:
            if(curr_node.right == None):
                curr_node.right = Node(data)
            else:
                self._insert(curr_node.right, data)
    
    def inorder(self):
        self._inorder(self.root)
        print()
            
    def _inorder(self, curr_node):
        if(curr_node):
            self._inorder(curr_node.left)
            print(curr_node.data, end = " ")
            self._inorder(curr_node.right)
            
    
t = tree()
t.insert_level(10)
t.inorder()
t.insert_level(11)
t.inorder()
t.insert_level(1)
t.inorder()
t.insert_level(13)
t.inorder()