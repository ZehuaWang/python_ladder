# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:52:13 2020

@author: ewang
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.buildTree_helper(preorder, inorder)
    
    def buildTree_helper(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        val = preorder[0]
        root = TreeNode(val)
        index = inorder.index(val)
        root.left = self.buildTree_helper(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree_helper(preorder[index+1:], inorder[index+1:])
        return root
        
        
