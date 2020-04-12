# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:50:36 2020

@author: ewang
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = self.list_to_int(digits) + 1
        print(num)
        return self.int_to_list(num)
    
    def list_to_int(self, digits):
        res = 0
        for i in range(len(digits)):
            res = res + digits[len(digits)-1-i] * (10**i)
        return res
    
    def int_to_list(self, num):
        res = []
        while num != 0:
            res.append(num % 10)
            num = num // 10
        res.reverse()
        return res
            
            
s = Solution()
print(s.plusOne([9,9,9]))

    
