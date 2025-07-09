class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Sliding window to process efficently and enforce the k indices apart constraint.
        seen = set()
        for i, num in enumerate(nums):
            if(num in seen):
                return True
            seen.add(num)
            if(len(seen) > k):
                seen.remove(nums[i-k]) # Size k Space complexity O(k)
        return False
