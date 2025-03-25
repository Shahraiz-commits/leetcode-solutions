class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS can be used to detect a cycle in a directed and undirected graph
        # Queue for BFS and stack for DFS
        
        visited = set()

        def bfs(r, c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))

            while queue:
                row,col = queue.popleft()
                directions = [[0,1],[1,0],[-1,0],[0,-1]] # Check neighbours
                for dr, dc in directions:
                    r,c = row+dr, col+dc
                    inside_grid = r in range(rows) and c in range(cols) 
                    if(inside_grid and grid[r][c]=="1" and (r,c) not in visited):
                        queue.append((r,c))
                        visited.add((r,c))

        rows = len(grid)
        cols = len(grid[0])
        count=0
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == "1" and (r,c) not in visited):
                    bfs(r,c)
                    count+=1 # Island found
        return count
