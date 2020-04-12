# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 13:36:16 2020

@author: ewang
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        while self.check_satisfy(nums) == False:
            for i in range(len(nums)):
                if nums[i] == 0:
                    for j in range(i, len(nums)):
                        if nums[j] != 0:
                            nums[i],nums[j] = nums[j],nums[i]
                            break
        return nums
        
    def check_satisfy(self, nums):
        print(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i, len(nums)):
                    if nums[j] != 0:
                        return False
        return True
        
        
s = Solution()
print(s.check_satisfy([1,0,1]))

