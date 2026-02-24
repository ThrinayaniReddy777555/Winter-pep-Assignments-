from collections import deque

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = "0"   # mark visited
            
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            while queue:
                row, col = queue.popleft()
                
                for dr, dc in directions:
                    new_r = row + dr
                    new_c = col + dc
                    
                    if (0 <= new_r < rows and 
                        0 <= new_c < cols and 
                        grid[new_r][new_c] == "1"):
                        
                        grid[new_r][new_c] = "0"
                        queue.append((new_r, new_c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
        
        return islands