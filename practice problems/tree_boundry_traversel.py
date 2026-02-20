# Node Structure (provided by GFG environment)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def isLeaf(self, node):
        return node.left is None and node.right is None

    def addLeftBoundary(self, root, res):
        curr = root.left
        while curr:
            if not self.isLeaf(curr):
                res.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
    
    def addLeaves(self, root, res):
        if self.isLeaf(root):
            res.append(root.data)
            return
        if root.left:
            self.addLeaves(root.left, res)
        if root.right:
            self.addLeaves(root.right, res)

    def addRightBoundary(self, root, res):
        curr = root.right
        temp = []
        while curr:
            if not self.isLeaf(curr):
                temp.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        for i in range(len(temp) - 1, -1, -1):
            res.append(temp[i])

    def boundaryTraversal(self, root):
        res = []
        if not root:
            return res
        
        if not self.isLeaf(root):
            res.append(root.data)
        
        self.addLeftBoundary(root, res)
        self.addLeaves(root, res)
        self.addRightBoundary(root, res)
        
        return res

