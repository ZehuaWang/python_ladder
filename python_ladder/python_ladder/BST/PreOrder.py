# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        
        res = []
        self.preorder_helper(root, [], res)
        return self.get_node_val(res)
    
    def get_node_val(self, list):
        res = []
        for ele in list:
            res.append(ele.val)
        return res
    
    def preorder_helper(self,node,visit_stack,res):
        if node not in res:
            res.append(node)
            visit_stack.append(node)
        
        if len(visit_stack) == 0:
            return
        
        if node.left != None:
            self.preorder_helper(node.left, visit_stack,res)

        if node.right != None:
            self.preorder_helper(node.right, visit_stack, res)

        if (node.right == None and node.left == None) or node in visit_stack:
            visit_stack.pop()
            
            if len(visit_stack) == 0:
                return
            else:
                self.preorder_helper(visit_stack[-1], visit_stack, res)
                
    def preorder_helper_simple(self, node, res):
        if node is not None:
            res.append(node.val)
            res = self.preorder_helper_simple(node.left,res)
            res = self.preorder_helper_simple(node.right, res)
        return res
    