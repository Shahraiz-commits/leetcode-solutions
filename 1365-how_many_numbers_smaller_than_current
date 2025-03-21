class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Sort the list so at index 2, we know it has 2 numbers less than it
        sorted_list = sorted(nums)
        hash = {}
        ret = []
        # [1,2,2,3,8]
        for index, num in enumerate(sorted_list):
            if num not in hash:
                hash[num] = index # 8:0 i.e. 8 has nothing less than it
        
        for num in nums:
            ret.append(hash[num])
        return ret
        
