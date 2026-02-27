import heapq

class Solution:
    def dijkstra(self, V, edges, S):
        
        # Step 1: Convert edge list to adjacency list
        adj = [[] for _ in range(V)]
        
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))  # remove this line if graph is directed
        
        # Step 2: Standard Dijkstra
        dist = [float('inf')] * V
        dist[S] = 0
        
        pq = [(0, S)]
        
        while pq:
            curr_dist, u = heapq.heappop(pq)
            
            if curr_dist > dist[u]:
                continue
            
            for v, wt in adj[u]:
                if dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
                    heapq.heappush(pq, (dist[v], v))
        
        return dist