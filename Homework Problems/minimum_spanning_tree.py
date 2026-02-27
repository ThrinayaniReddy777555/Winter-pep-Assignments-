class Solution:
    def spanningTree(self, V, edges):
        
        # Step 1: Sort edges by weight
        edges.sort(key=lambda x: x[2])
        
        parent = list(range(V))
        rank = [0] * V
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            
            if rootX == rootY:
                return False  # Cycle
            
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            
            return True
        
        total_weight = 0
        
        for u, v, wt in edges:
            if union(u, v):
                total_weight += wt
        
        return total_weight