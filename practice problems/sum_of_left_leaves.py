# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:#type: ignore 
        if not root:
            return 0
        ans=0
        if root.left:
            if not root.left.right and not root.left.left:
                ans+=root.left.val
            else:
                self.sumOfLeftLeaves(root.left)
        ans+=self.sumOfLeftLeaves(root.right)
        return ans
        