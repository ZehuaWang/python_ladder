# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        #if len(inorder) == 0 or len(postorder) == 0:
        #    return None
        
        #root = TreeNode(postorder[len(postorder) - 1])
        #postorder = postorder[:-1]
        #self.buildTree_helper(inorder, postorder, root)
        return self.buildTree_helper_recur(inorder,postorder)
    
    def buildTree_helper_recur(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        val = postorder[-1]
        root = TreeNode(val)
        index = inorder.index(val)
        root.left = self.buildTree_helper_recur(inorder[:index], postorder[:index])
        root.right = self.buildTree_helper_recur(inorder[index+1:], postorder[index:-1])
        return root
        
    def buildTree_helper(self, inorder, postorder, root): # root (3) postorder [2,1,4] inorder[1,2,3,4]
        if len(postorder) != 0:
            inorder_pointer = inorder.index(root.val)
            
            left_array = inorder[0:inorder_pointer]
            right_array = inorder[inorder_pointer+1:]
            
            if len(right_array) == 1:
                temp_node = TreeNode(right_array[0])
                root.right = temp_node
                postorder.remove(right_array[0])
                
            if len(left_array) == 1:
                temp_node = TreeNode(left_array[0])
                root.left = temp_node
                postorder.remove(left_array[0])
                
            if len(left_array) > 1:
                temp_node_val = self.find_first_from_back(postorder, left_array)
                temp_node = TreeNode(temp_node_val)
                root.left = temp_node
                postorder.remove(temp_node.val)
                self.buildTree_helper(left_array, postorder, temp_node)
                
            if len(right_array) > 1:
                temp_node_val = self.find_first_from_back(postorder, right_array)
                temp_node = TreeNode(temp_node_val)
                root.right = temp_node
                postorder.remove(temp_node.val)
                self.buildTree_helper(right_array, postorder, temp_node)
        
        return
    
    def find_first_from_back(self, postorder, inorder):
        for i in range(len(postorder)):
            if (postorder[len(postorder) - i - 1] in inorder):
                return postorder[len(postorder) - i - 1]