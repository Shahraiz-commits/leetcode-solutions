class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        lastChar = '' # Last seen character to determine dupes
        for i in range(len(nums)):
            if(nums[i] != lastChar):
                lastChar = nums[i]
                nums[k] = nums[i]
                k+=1
        nums = nums[:k]
        return k
