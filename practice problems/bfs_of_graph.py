from collections import deque


class Solution:
    def bfs(self, adj):
        visited = set()
        q = deque([0])
        visited.add(0)
        res = []

        while q:
            node = q.popleft()
            res.append(node)

            for nbr in adj[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    q.append(nbr)

        return res