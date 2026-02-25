class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        rows, cols = len(image), len(image[0])
        old_color = image[sr][sc]
        
        # If the start pixel already has the new color, no need to fill
        if old_color == color:
            return image
        
        def dfs(r, c):
            # Base case: if out of bounds or not the original color, stop
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                image[r][c] != old_color):
                return
            
            # Update color
            image[r][c] = color
            
            # Check 4-directional neighbors
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(r + dr, c + dc)
        
        dfs(sr, sc)
        return image