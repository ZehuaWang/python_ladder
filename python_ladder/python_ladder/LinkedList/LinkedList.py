# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 16:42:19 2020

@author: ewang
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_after_node(self, prev_node, data):
        
        if not prev_node:
            return
        
        new_node = Node(data)
        
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        
        if cur_node is None:
            return
        
        prev.next = cur_node.next
        cur_node = None
        
    def delete_node_at_pos(self, pos):
        cur_node = self.head
        
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        
        prev = None
        count = 1
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        
        if cur_node is None:
            return
        
        prev.next = cur_node.next
        cur_node = None
    
    def len_iterative(self):
        
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count
    
    def len_recursive(self,node):
        if node is None:
            return 0
        if node.next == None:
            return 1
        else:
            return 1 + self.len_recursive(node.next)        
        
list = LinkedList()
list.append("a")
list.append("b")
list.insert_after_node(list.head.next, "e")
list.append("c")
list.delete_node("b")
list.print_list()
print(list.len_recursive(list.head))