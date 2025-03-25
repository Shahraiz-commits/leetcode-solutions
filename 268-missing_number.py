class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_in_order = range(len(nums)+1) # [3,0,1] -> 0,1,2,3 Expected
        return sum(nums_in_order) - sum(nums) # 6 - 4  = 2
