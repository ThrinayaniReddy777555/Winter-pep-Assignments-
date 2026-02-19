# '''
# class Node:
#     def _init_(self,val):
#         self.data = val
#         self.left = None
#         self.right = None
# '''
# class Solution:
#     def KDistance(self, root, k):
#         result=[]
#         if k < 0 or not root:
#             return
        
#         if root and k == 0:
#             self.result.append(root.data)
        
#         self.KDistance(root.left, k - 1)
#         self.KDistance(root.right, k - 1)
        
#         return self.result

class Solution:
    def KDistance(self, root, k):
        self.result = []
        
        self.find_nodes(root, k)
        
        return self.result

    def find_nodes(self, root, k):
        if not root or k < 0:
            return
        
        if k == 0:
            self.result.append(root.data)
            return
            
        self.find_nodes(root.left, k - 1)
        self.find_nodes(root.right, k - 1)

  