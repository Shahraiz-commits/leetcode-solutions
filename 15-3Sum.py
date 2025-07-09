class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # [-4, -1, -1, 0, 1, 2]
        ret = []
        for i in range(len(nums) - 1):
            fixed = nums[i]
            if(fixed > 0): # Cannot possibly add up to 0
                break
            l = i+1
            r = len(nums) - 1
            if(i>0 and fixed == nums[i-1]):
                continue # Duplicate
            while(l < r):
                sum = fixed + nums[l] + nums[r]
                if(sum < 0): # Need to increase total value
                    l+=1
                elif(sum > 0): # Need to decrease total value
                    r-=1
                else:
                    ret.append([nums[l], nums[r], fixed])
                    l+=1
                    while(l<r and nums[l] == nums[l-1]):
                        l+=1
                    
        return ret
