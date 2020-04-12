# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:27:44 2020

@author: ewang
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    
    def inorder_helper(self, start, res):
        if start not None:
            res = self.inorder_helper(start.left, res)
            res.append(start.val)
            res = self.inorder_helper(start.right, res)
        return res