# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class Solution:
#     def invertTree(self, root: TreeNode | None) -> TreeNode | None:
#         if not root:
#             return None

#         left = self.invertTree(root.left)
#         right = self.invertTree(root.right)

#         root.left = right
#         root.right = left

#         return root
            #DFS approach 
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:#type: ignore 
        if not root:
            return None
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
