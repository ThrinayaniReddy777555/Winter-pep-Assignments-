class Solution:
    def dfs(self, adj):
        n = len(adj)
        v = [False] * n
        res = []
        def solve(u):
            v[u] = True
            res.append(u)
            for e in adj[u]:
                if not v[e]:
                    solve(e)
        solve(0)   
        return res