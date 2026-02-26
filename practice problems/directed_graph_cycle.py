class Solution:
    def dfs(self, adj_list, start_vtx, visited, path_visited):
        visited[start_vtx] = True
        path_visited[start_vtx] = True
        
        for adj_vtx in adj_list[start_vtx]:
            if not visited[adj_vtx]:
                if self.dfs(adj_list, adj_vtx, visited, path_visited):
                    return True
            elif path_visited[adj_vtx]:
                return True
        
        path_visited[start_vtx] = False
        return False
     
    def isCyclic(self, V, edges):
        # code here
        
        if not edges:
            return False
        
        adj_list = [[] for _ in range(V)]
        
        for edge in edges:
            frm = edge[0]
            to = edge[1]
            adj_list[frm].append(to)
        
        visited = [False] * V
        path_visited = [False] * V
        
        for vtx in range(V):
            if not visited[vtx]:
                if self.dfs(adj_list, vtx, visited, path_visited):
                    return True
        return False