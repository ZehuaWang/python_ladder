# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:42:57 2020

@author: ewang
"""
class Stack():
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items

def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0
    
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
            index += 1
            
    if s.empty() and is_balanced:
        return True
    else:
        return False
    
def is_match(p1,p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True    
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

is_paren_balanced("()")
