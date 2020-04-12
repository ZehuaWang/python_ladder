class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        res = []
        for i in range(len(nums)):
            if nums[i] in dict:
                res = [nums.index(target-nums[i]), i]
                break
            else:
                dict[target-nums[i]] = nums[i]
        return res