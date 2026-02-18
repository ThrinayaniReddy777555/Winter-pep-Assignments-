class Solution:
    def getLevel(self, root, target):
        return self._find_level(root, target, 1)

    def _find_level(self, node, target, level):
        if node is None:
            return 0 
        
        if node.data == target:
            return level  
        res = self._find_level(node.left, target, level + 1)
        if res != 0:
            return res

        return self._find_level(node.right, target, level + 1)
