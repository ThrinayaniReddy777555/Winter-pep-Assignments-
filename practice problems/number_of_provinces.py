class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def dfs(city):
            # Mark the current city as visited
            visited[city] = True
            # Iterate through all potential neighbors
            for neighbor in range(n):
                # If there is a connection and the neighbor hasn't been visited
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        for i in range(n):
            # If the city hasn't been visited, it means we found a new province
            if not visited[i]:
                dfs(i)
                provinces += 1 # Increment the count for the new province
        
        return provinces
