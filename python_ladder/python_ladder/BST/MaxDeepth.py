# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    answer = 0
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #cur_depth = 1
        #self.max_deepth_helper(root, cur_depth)
        #return self.answer
        return self.max_deepth_helper_bttom_up(root)
        
    def max_deepth_helper(self, root, cur_depth):
        if root == None:
            return
        
        if root.left == None and root.right == None:
            self.answer = max(self.answer, cur_depth)
            
        self.max_deepth_helper(root.left, cur_depth+1)
        self.max_deepth_helper(root.right, cur_depth+1)
        
    def max_deepth_helper_bttom_up(self, root):
        if root is None:
            return 0
        
        left_depth = self.max_deepth_helper_bttom_up(root.left)
        right_depth = self.max_deepth_helper_bttom_up(root.right)
        
        return max(left_depth, right_depth) + 1
                
            
            
            
        


