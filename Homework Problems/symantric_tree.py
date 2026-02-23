# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool: # type: ignore
        # Initial call to the helper function, comparing the left and right children of the root
        return self.isMirror(root.left, root.right)

    def isMirror(self, left_node: Optional[TreeNode], right_node: Optional[TreeNode]) -> bool: # type: ignore
        # Base case 1: If both nodes are None, they are symmetric
        if not left_node and not right_node:
            return True
        # Base case 2: If only one of the nodes is None, they are not symmetric
        if not left_node or not right_node:
            return False
        # Base case 3: If the node values are different, they are not symmetric
        if left_node.val != right_node.val:
            return False
        
        # Recursive step:
        # Check if the left child of the left node mirrors the right child of the right node,
        # AND if the right child of the left node mirrors the left child of the right node
        return self.isMirror(left_node.left, right_node.right) and self.isMirror(left_node.right, right_node.left)
