# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:#type: ignore 
        ans=0
        def maxDepth(root: TreeNode | None):#type: ignore
            nonlocal ans
            if not root:
                return 0

            l=maxDepth(root.left)
            m=maxDepth(root.right)
            ans=max(ans,l+m)
            return 1+max(l,m)
        maxDepth(root)
        return ans
      
        