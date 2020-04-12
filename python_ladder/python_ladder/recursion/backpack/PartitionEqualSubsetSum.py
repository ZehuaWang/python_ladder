# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:29:33 2020

@author: ewang
"""
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        
        if self.get_list_sum(nums) %2 != 0:
            return False
        
        target = self.get_list_sum(nums) / 2
        return self.validate(target,self.genSubsets(nums))
    
    def get_list_sum(self,nums):
        res = 0
        for num in nums:
            res = res + num
        return res
    
    def genSubsets(self, L):
        res = []
        if len(L) == 0:
            return [[]] # list of empty list
        smaller = self.genSubsets(L[:-1]) # all subsets without last element
        extra = L[-1:] # create a list of just last element
        new = []

        for small in smaller:
            new.append(small+extra) # for all smaller solutions, add one with last element
            
        return smaller+new
    
    def validate(self, target, input_list):
        for list in input_list:
            if target == self.get_list_sum(list):
                return True
        return False
    
#nums = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
nums = [1,1,1,1]
s = Solution()
print(s.canPartition(nums))
        