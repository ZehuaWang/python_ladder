# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:25:05 2020

@author: ewang
"""
class Stack(object):
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def size(self):
        return len(self.items)
    
    def __len__(self):
        return self.size()


class Queue(object):
    def __init__(self):
        self.items = []
    
    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
        
    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.items)

class Node(object):
    def __init__(self, value):
        self.value = value
        
        self.left = None
        self.right = None
class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)
        
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        else:
            print("Traversal type " + str(traversal_type) + "is not supported.")
    # depth first search
    # pre-order in-order post-order        
    def preorder_print(self, start, traversal):
        """" root -> left -> right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
    def inorder_print(self, start, traversal):
        """left -> root -> right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal
    
    def postorder_print(self, start, traversal):
        """"left -> right -> root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal
    
    def reverse_levelorder_print(self, start):
        if start is None:
            return
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        
        traversal = ""
        
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)
            
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
                
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"
            
        return traversal

    # breadth-first search
    def levelorder_print(self,start):
        if start:
            visit_queue = []
            visit_queue.append([start])
            res = []
            res.append([start.value])
            
            # for child in visit_queue:
            #     level_res = []
            #     if child.left:
            #         visit_queue.append(child.left)
            #         level_res.append(child.left.value)
            #     if child.right:
            #         visit_queue.append(child.right)
            #         level_res.append(child.right.value)
                
            #     if len(level_res) != 0:
            #         res.append(level_res)
                
            #     visit_queue.pop()
            
            while visit_queue:
                children = visit_queue.pop()
                level_res = []
                level_visit_queue = []
                
                for child in children:
                    if child.left:
                        level_visit_queue.append(child.left)
                        level_res.append(child.left.value)
                    if child.right:
                        level_visit_queue.append(child.right)
                        level_res.append(child.right.value)
                
                if len(level_visit_queue) != 0:
                    visit_queue.append(level_visit_queue)
                
                if len(level_res) != 0:
                    res.append(level_res)
                        
            return res
            
        
            
                    
                
    

#     1
#    /  \
#   2    3
#  / \  /  \
# 4  6 7   5
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
#tree.root.left.left = Node(4)
#tree.root.left.right = Node(6)
tree.root.right.left = Node(7)
tree.root.right.right = Node(5)

print(tree.levelorder_print(tree.root))
print(tree.reverse_levelorder_print(tree.root))
