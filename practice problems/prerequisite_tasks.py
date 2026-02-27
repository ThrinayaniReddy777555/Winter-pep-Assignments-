from collections import deque

class Solution:
    def isPossible(self, N, P, prerequisites):
        
        # Build graph
        graph = [[] for _ in range(N)]
        indegree = [0] * N
        
        for pair in prerequisites:
            u = pair[0]
            v = pair[1]
            
            # Safety check (optional for debugging)
            if u >= N or v >= N:
                return False
            
            graph[v].append(u)
            indegree[u] += 1
        
        # Kahn's Algorithm
        q = deque()
        for i in range(N):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0
        
        while q:
            node = q.popleft()
            count += 1
            
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return count == N