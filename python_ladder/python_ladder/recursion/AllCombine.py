# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 21:06:58 2020

@author: ewang
"""
class Solution(object):
    
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        all_combine_list = self.combine_helper(n)
        res_list = self.filter_element_with_length(all_combine_list,k)
        return res_list
        
    def combine_helper(self,n):
        if n == 0:
            list = [[]]
            return list
        else:
            res_list = self.combine_helper(n-1)
            tmp_list = self.combine_helper(n-1)[:]
            for element in tmp_list:
                tmp_element = element[:]
                tmp_element.append(n)
                res_list.append(tmp_element)
            return res_list
    
    def filter_element_with_length(self,list,k):
        res = []
        for element in list:
            if len(element) == k:
                res.append(element)
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
        
s = Solution()
#print(s.combine(5,2))
#print(s.genSubsets([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))

