# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right  
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        left = root
        right = root
        hl = 0
        hr = 0
        while left:
            hl += 1
            left = left.left
        while right:
            hr += 1
            right = right.right
        if hl == hr:
            return (1 << hl) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)