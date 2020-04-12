# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    #tree_path_list = []
    
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        tree_path_list = []
        self.get_path_helper(root,[root.val],tree_path_list)
        print(tree_path_list)
        return self.check_sum(tree_path_list,sum)
    
    def get_path_helper(self, root, previous_path, tree_path_list):
        if root == None:
            return
        
        if root.left == None and root.right == None:
            tree_path_list.append(previous_path)
                
        if root.left:
            temp_path = previous_path[:]
            temp_path.append(root.left.val)
            self.get_path_helper(root.left, temp_path, tree_path_list)
            
        if root.right:
            temp_path = previous_path[:]
            temp_path.append(root.right.val)
            self.get_path_helper(root.right,temp_path, tree_path_list)
            
    def check_sum(self, list_of_list, target):
        for list in list_of_list:
            if sum(list) == target:
                return True
        return False