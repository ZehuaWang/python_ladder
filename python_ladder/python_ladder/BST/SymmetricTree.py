# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    tree_path_list = []
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        #visit_queue = [[root]]
        #res = [[root.val]]
        #ans = self.is_symmetric_helper(root,visit_queue,res)
        #is_symmetric = self.check_symmetric_list(ans)
        #return is_symmetric
        
        self.is_symmetric_helper_recursive(root,[root.val])
        print(self.tree_path_list)
        return self.check_is_symmetric_for_iterative_method(self.tree_path_list)
        
    def is_symmetric_helper(self, root, visit_queue, res):
        while len(visit_queue) != 0:
            children = visit_queue.pop()
            temp_res = []
            temp_visit_queue = []
            for child in children:
                if child.left:
                    temp_visit_queue.append(child.left)
                    temp_res.append(child.left.val)
                else:
                    temp_res.append(None)              
                    
                if child.right:
                    temp_visit_queue.append(child.right)
                    temp_res.append(child.right.val)
                else:
                    temp_res.append(None)
                    
            if len(temp_res) != 0:
                res.append(temp_res)
            
            if len(temp_visit_queue) != 0:
                visit_queue.append(temp_visit_queue)
        return res
    
    def check_symmetric_list(self,ans_list):
        ans_list.pop(0)
        
        for element in ans_list:
            if len(element) % 2 != 0:
                return False
            
            for i in range(len(element)):
                if element[i] != element[len(element) - 1 - i]:
                    return False
        
        return True
    
    #----------------------recursive----------------------
    def is_symmetric_helper_recursive(self,root,previous_path):
        
        if root == None:
            return
        if root.left == None and root.right == None:
            self.tree_path_list.append(previous_path)
        
        if root.left:
            temp_path = previous_path[:]
            temp_path.append(root.left.val)
            self.is_symmetric_helper_recursive(root.left, temp_path)
        if root.right:
            temp_path = previous_path[:]
            temp_path.append(root.right.val)
            self.is_symmetric_helper_recursive(root.right, temp_path)
            
    def check_is_symmetric_for_iterative_method(self, list):
        for i in range(len(list)):
            if list[i] != list[len(list) - 1 - i]:
                return False
        return True
        
    
        
    
    
        