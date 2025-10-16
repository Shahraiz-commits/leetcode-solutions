class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]  # (n-2) x (n-2) output matrix

        for i in range(n - 2):          # slide vertically
            for j in range(n - 2):      # slide horizontally
                max_val = 0
                # Look at the 3x3 window starting at (i, j)
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        max_val = max(max_val, grid[x][y])
                res[i][j] = max_val     # store max of this 3x3 window

        return res

