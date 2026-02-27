from collections import deque

class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        
        n = len(graph)
        color = [-1] * n  # -1 = uncolored
        
        for start in range(n):
            if color[start] == -1:
                
                queue = deque([start])
                color[start] = 0
                
                while queue:
                    node = queue.popleft()
                    
                    for neighbor in graph[node]:
                        
                        if color[neighbor] == -1:
                            # Assign opposite color
                            color[neighbor] = 1 - color[node]
                            queue.append(neighbor)
                        
                        elif color[neighbor] == color[node]:
                            return False
        
        return True