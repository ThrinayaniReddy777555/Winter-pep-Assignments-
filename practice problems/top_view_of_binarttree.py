from collections import deque
        #BFS
class Solution:
    def topView(self, root):
        if not root:
            return []
        
        hd_map = {}
        queue = deque([(root, 0)])
        
        while queue:
            node, hd = queue.popleft()
            
            if hd not in hd_map:
                hd_map[hd] = node.data
            
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        
        result = []
        for key in sorted(hd_map.keys()):
            result.append(hd_map[key])
        
        return result
    
#we will not use