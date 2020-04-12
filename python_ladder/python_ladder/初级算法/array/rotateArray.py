# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 20:42:33 2020

@author: ewang
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        res_nums = [0] * len(nums)
        
        for i in range(len(nums)):
            res_nums[(i+k) % len(nums)] = nums[i]
            
        return res_nums
    
    def rotate_size_slice(self, nums, k):
        k = k % len(nums)
        #nums = nums[-k:] + nums[:-k] #no pass
        nums[:k],nums[k:] = nums[len(nums) - k:], nums[:len(nums)-k]
        return nums
        
        
s = Solution()
print(s.rotate([1,2,3,4,5,6,7] , 3))
print(s.rotate_size_slice([1,2,3,4,5,6,7] , 3)) 