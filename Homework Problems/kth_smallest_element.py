# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int: # type: ignore
        stack = []
        while root or stack:
            # Go as far left as possible, pushing nodes onto the stack
            while root:
                stack.append(root)
                root = root.left
            
            # Process the next smallest node
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            
            # Move to the right subtree to find the next smallest
            root = root.right
