class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 90 = transpose + reverse row
        # 180 = reverse row + reverse column
        # 270 = transpose + reverse col

        # Transpose in place
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        
        # Reverse rows order = matrix[::-1]
        # Reverse cols order = matrix[:, ::-1]
        # Reverse columns = matrix.reverse()
        for row in matrix:
            row.reverse()

