class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Dynamic sliding window where window decreases everytime we find our target to look for a smaller subarray sol
        total=0
        l=0
        min_len = float(inf)
        for r in range(len(nums)):
            total += nums[r]
            while(total >= target):
                min_len = min(min_len, r-l+1)
                total -= nums[l]
                l+=1
        if(min_len == float(inf)):
            return 0
        else:
            return min_len
