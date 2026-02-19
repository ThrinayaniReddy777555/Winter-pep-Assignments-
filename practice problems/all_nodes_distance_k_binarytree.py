from collections import deque

class Solution:
    def distanceK(self, root, target, k):
        parent = {}
        
        def dfs(node, par):
            if not node:
                return
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)
        
        queue = deque([(target, 0)])
        visited = set([target])
        result = []
        
        while queue:
            node, dist = queue.popleft()
            
            if dist == k:
                result.append(node.val)
            
            elif dist < k:
                for nei in (node.left, node.right, parent[node]):
                    if nei and nei not in visited:
                        visited.add(nei)
                        queue.append((nei, dist + 1))
        
        return result