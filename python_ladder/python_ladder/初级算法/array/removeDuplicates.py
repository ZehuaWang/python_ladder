class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Use two pointers
        head_pointer = 0
        
        for i in range(len(nums)):
            if nums[i] != nums[head_pointer]:
                head_pointer = head_pointer + 1
                nums[head_pointer] = nums[i]
                
        return head_pointer+1
    
s = Solution()
print(s.removeDuplicates([0,0,0,0,1,1,1,2,2,3,3,4]))