# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = [root.val]
        visit_queue = [root]
        self.levelOrder_helper(visit_queue, res)
        return res
        
    def levelOrder_helper(self, visit_queue, res):
        if len(visit_queue) != 0:
            temp = []
            for element in visit_queue[:]:
                if element.left != None:
                    temp.append(element.left.val)
                    visit_queue.append(element.left)
                if element.right != None:
                    temp.append(element.right.val)
                    visit_queue.append(element.right)
                visit_queue.remove(element)
            if len(temp) != 0:
                res.append(temp)
            self.levelOrder_helper(visit_queue,res)
        else:
            return 
                
            
                
        
            
            