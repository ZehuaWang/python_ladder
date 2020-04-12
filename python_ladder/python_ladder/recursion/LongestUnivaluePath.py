# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:35:59 2020

@author: ewang
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        if root.left == None:
            return
        if root.right == None:
            return
        if root.left == root.right:
            self.ans = self.ans + 1
            self.longestUnivaluePath(root.left)
            self.longestUnivaluePath(root.right)
        return self.ans
    
class node:
    def __init__(self,value=None):
        self.value = value
        self.left_child=None
        self.right_child=None
    
class binary_search_tree:
    def __init__(self):
        self.root=None
    
    def insert(self,value):
        if self.root == None:
            self.root=node(value)
        else:
            self._insert(value,self.root)
    
# object

class Coordinate(object):
    # attributes
    def __init__(self,x,y):
        self.x = x  
        self.y = y
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def __str__(self):
        return ("<"+str(self.x)+","+str(self.y)+">")
    # data atributes
     
    # methods
c = Coordinate(3,4)
origin = Coordinate(0,0)
print(c.x)
print(origin.x)
print(c.distance(origin))
print(Coordinate.distance(c,origin))
print(c)
print(type(c))
print(isinstance(c,Coordinate))