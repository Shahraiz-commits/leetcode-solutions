class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ret = []
        min_diff = float('inf') # Infinity

        # Find min difference
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i-1])
            
            
        for i in range(1, len(arr)):
            if(abs(arr[i] - arr[i-1]) == min_diff):
                ret.append([arr[i-1], arr[i]])
        return ret
