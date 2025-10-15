class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                inBounds = i-1 >= 0 and j-1 >= 0
                if inBounds and matrix[i-1][j-1] != matrix[i][j]:
                    return False
        return True  
