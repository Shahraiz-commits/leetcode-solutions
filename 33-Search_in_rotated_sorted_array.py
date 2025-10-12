class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch(left, right):
            while(left <= right):
                mid = (left + right) // 2
                if(target == nums[mid]):
                    return mid
                if(target < nums[mid]):
                    right = mid - 1
                if(target > nums[mid]):
                    left = mid + 1
            return -1

        # Find pivot
        pivot = -1
        for i in range(len(nums)-1):
            if(nums[i] > nums[i+1]):
                pivot = i
                break
        # No rotation
        if(pivot == -1):
            return binarySearch(0, len(nums)-1)
        else:
            # Search left half
            ret = binarySearch(0, pivot)
            if(ret == -1):
                # Search right half
                return binarySearch(pivot+1, len(nums)-1)
            else:
                return ret
