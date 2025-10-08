class Solution:
    def maxArea(self, height: List[int]) -> int:
        # l and r pointers greedy with min of the two points * j-i
        max_volume = 0
        l, r = 0, len(height) - 1 
        while(r > l):
            x = r - l
            y = min(height[l], height[r])
            volume = x * y
            max_volume = max(max_volume, volume)

            if(height[r] < height[l]):
                r -= 1
            else:
                l += 1

        return max_volume
