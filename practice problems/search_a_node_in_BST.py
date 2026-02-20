'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def search(self, root, key):
        result =[]
        if root==None:
            return False
        if key == root.data:
            return True
        elif key<root.data:
            return self.search(root.left,key)
        else:
            return self.search(root.right,key)
        # code here