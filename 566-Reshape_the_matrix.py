class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if(r*c != len(mat)*len(mat[0])):
            return mat
        
        ret = [[0] * c for _ in range(r)] # r x c resulting matrix
        nums = [num for row in mat for num in row]  # Flatten matrix
        
        k = 0
        for i in range(r):
            for j in range(c):
                ret[i][j] = nums[k]
                k += 1

        return ret
