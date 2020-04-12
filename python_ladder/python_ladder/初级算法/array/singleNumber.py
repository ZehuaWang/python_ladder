# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:27:30 2020

@author: ewang
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        valid_list = []
        result_list = []
        
        for i in nums:
            if i not in valid_list:
                valid_list.append(i)
            else:
                result_list.append(i)
        
        for i in nums:
            if i not in result_list:
                return i
            
s = Solution()
print(s.singleNumber([4,1,2,1,2]))