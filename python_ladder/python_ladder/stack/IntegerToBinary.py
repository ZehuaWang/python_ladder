# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 18:47:05 2020

@author: ewang
"""
from stack import Stack

def div_by_two(dec_num):
    s = Stack()
    
    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2
        
    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())
        
    return bin_num

print(div_by_two(242))
        
