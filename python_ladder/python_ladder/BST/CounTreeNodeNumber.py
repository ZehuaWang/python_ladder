# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        res_queue = [root.val]
        self.count_node_helper(root, [root], res_queue)
        return res_queue
        
    def count_node_helper(self, root, visit_queue, res_queue):
        while len(visit_queue) != 0:
            child = visit_queue.pop()
            
            if child.left:
                res_queue.append(child.left.val)
                visit_queue.append(child.left)
            if child.right:
                res_queue.append(child.right.val)
                visit_queue.append(child.right)