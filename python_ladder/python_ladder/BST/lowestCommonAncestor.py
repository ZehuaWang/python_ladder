# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        res_path = []
        self.get_path_for_nodes(root, [root.val], res_path, p.val, q.val)
        print(res_path)
        res = self.find_ancestor_from_list_of_list(res_path)
        return TreeNode(res)

    def get_path_for_nodes(self, root, previous_path, res_path, p, q):
        if root == None:
            return None
        
        if root.val == p:
            res_path.append(previous_path)
        
        if root.val == q:
            res_path.append(previous_path)
            
        if root.left:
            temp_previous_path = previous_path[:]
            temp_previous_path.append(root.left.val)
            self.get_path_for_nodes(root.left, temp_previous_path, res_path, p, q)
        
        if root.right:
            temp_previous_path = previous_path[:]
            temp_previous_path.append(root.right.val)
            self.get_path_for_nodes(root.right, temp_previous_path, res_path, p, q)

    def find_ancestor_from_list_of_list(self, tree_path_list):
        tree_path_one = tree_path_list[0]
        tree_path_two = tree_path_list[1]

        temp_path = []
        if len(tree_path_one) < len(tree_path_two):
            temp_path = tree_path_one
        else:
            temp_path = tree_path_two

        res = 0
        for i in range(len(temp_path)):
            if tree_path_one[i] != tree_path_two[i]:
                res = i
        res = res - 1
        return tree_path_one[res]