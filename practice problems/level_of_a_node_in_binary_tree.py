'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
# class Solution:

#     def getLevel(self, root, target):
#         '''
#         :param root: root of given tree.
#         :param target: target to find level
#         :return: LEVEL NO (or -1 if not found)
#         '''
#         if root is None:
#             return -1  

#         if root.data == target:
#             return 1  

#         left_level = self.getLevel(root.left, target)
#         if left_level != -1:
#             return left_level + 1 
#         right_level = self.getLevel(root.right, target)
#         if right_level != -1:
#             return right_level + 1
#         return -1 
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
