# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':#type: ignore 
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        node = root
        while node:
            # If both p and q are greater than the current node's value,
            # the LCA must be in the right subtree.
            if p.val > node.val and q.val > node.val:
                node = node.right
            # If both p and q are smaller than the current node's value,
            # the LCA must be in the left subtree.
            elif p.val < node.val and q.val < node.val:
                node = node.left
            # Otherwise, the current node is the LCA, as p and q are on opposite sides
            # or one of them is the current node itself.
            else:
                return node
        return None # Should not be reached given problem constraints

