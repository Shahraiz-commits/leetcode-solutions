class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        goingDown = False
        ret = []
        i, j = 0, 0
        m, n = len(mat), len(mat[0])
        size = m * n

        while len(ret) < size:
            ret.append(mat[i][j])

            if goingDown:
                # Moving down-left
                if i == m - 1:      # bottom edge
                    j += 1
                    goingDown = False
                elif j == 0:        # left edge
                    i += 1
                    goingDown = False
                else:
                    i += 1
                    j -= 1
            else:
                # Moving up-right
                if j == n - 1:      # right edge
                    i += 1
                    goingDown = True
                elif i == 0:        # top edge
                    j += 1
                    goingDown = True
                else:
                    i -= 1
                    j += 1

        return ret

