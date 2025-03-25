class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ret=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if(grid[r][c] == 1):
                    ret+=4
                    if(r>0 and grid[r-1][c]==1):
                        ret-=2
                    if(c>0 and grid[r][c-1]==1):
                        ret-=2
        return ret
