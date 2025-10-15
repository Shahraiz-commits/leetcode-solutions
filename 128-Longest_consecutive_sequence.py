class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums) # For O(1) lookup
        best = 0
        for num in nums:
            if num-1 not in nums: # New sequence
                y = num
                while(y in nums):
                    y+=1
                currLen = y-num
                best = max(best, currLen)
        return best
