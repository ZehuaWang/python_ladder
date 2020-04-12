# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:42:49 2020

@author: ewang
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        if len(nums1) <= len(nums2):
            for num in nums1:
                if num in nums2:
                    nums2.remove(num)
                    res.append(num)
        return res

s = Solution()
print(s.intersect([4,9,5],[9,4,9,8,4]))