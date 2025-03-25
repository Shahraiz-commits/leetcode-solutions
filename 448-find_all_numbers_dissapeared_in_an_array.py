class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        max = len(nums)+1
        nums = set(nums)
        ret = []
        for i in range(1, max):   
            if i not in nums:
                ret.append(i)
        return ret
        
