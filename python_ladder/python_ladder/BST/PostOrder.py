# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:37:56 2020

@author: ewang
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.postorder_helper(root,[])
    def postorder_helper(self, node, res):
        if node:
            res = self.postorder_helper(node.left, res)
            res = self.postorder_helper(node.right, res)
            res.append(node.val)
        return res