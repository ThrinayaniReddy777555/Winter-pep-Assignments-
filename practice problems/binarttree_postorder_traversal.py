# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]: # type: ignore
        ans = []
        def postorder(root: Optional[TreeNode]) -> None: # type: ignore
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            ans.append(root.val)
        
        postorder(root)
        return ans        