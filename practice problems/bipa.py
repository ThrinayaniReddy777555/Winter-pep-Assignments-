from collections import defaultdict, deque #imported defaultdict subclass & deque subclass from collections module
class Solution:                     #Creating a solution class
    def isBipartite(self, V, edges):#defining bipartite graph function
        # code here
        color = [-1]*V #default is not colored
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)#add towards the end of x
            graph[y].append(x)#add towards the end of y
        for start in range(V):
            if color[start] == -1: #not colored yet
                w = deque([start])
                color[start] = 0 #colored with 0
                while w:
                    node = w.popleft()#removes and returns an element from the left end
                    for neighbor in graph[node]:
                        if color[neighbor] == -1: #if neighbor is not colored
                            color[neighbor] = 1 - color[node]#color it with 1
                            w.append(neighbor) #append neighbor into the queue
                        elif color[neighbor] == color[node]: #check if neigh color == node, return false if so
                            return False
        return True