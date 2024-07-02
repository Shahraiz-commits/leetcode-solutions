class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counter = 0
        for n in nums:
            if counter < 0:
                return False
            elif n > counter:
                counter = n
            counter -= 1
            
        return True
