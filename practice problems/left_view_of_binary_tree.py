''' 
class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 
'''
            
class Solution:
    def leftView(self, root):
#         BFS 
#         if not root:
#             return 0
#         result =[]
#         queue=deque([root])
#         while queue:
#             level_size=len(queue)
#             for i in range(level_size):
#                 node=queue.popleft()
#                 if i == 0:
# result.append(node.data)
#                 if node.left:
# queue.append(node.left)
#                 if node.right:
# queue.append(node.right)
#         return result
        
#         code here
#         DFS
        result =[]
        def dfs(node,level):
            if not node:
                return 
            if level == len(result):
                result.append(node.data)
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        dfs(root,0)    
        return result
                    
        