# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 19:47:20 2020

@author: ewang
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_counter = 0
        res = 0
        for i in range(len(prices)):
            if prices[i] > prices[buy_counter]:
                res = res + prices[i] - prices[buy_counter]
            buy_counter = i
        return res
    
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
               
        
        