class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Memoize going from top left to bottom right looking for squares
        squares = {} # Index - max size of square ending here
        maxSizeOverall = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                elem = matrix[i][j]
                if(elem == '1'):
                    # Out of bounds
                    if i == 0 or j == 0:
                        squares[(i, j)] = 1
                    else:
                        squares[(i,j)] = 1 + min(squares.get((i-1, j), 0), squares.get((i, j-1), 0), squares.get((i-1, j-1), 0))
                    maxSizeOverall = max(maxSizeOverall, squares[(i,j)])
        return maxSizeOverall * maxSizeOverall
