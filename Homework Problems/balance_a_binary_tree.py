# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode: # type: ignore
        # Step 1: Perform in-order traversal to get sorted values
        vals = []
        def inorder_traversal(node):
            if not node:
                return
            inorder_traversal(node.left)
            vals.append(node.val)
            inorder_traversal(node.right)
        
        inorder_traversal(root)
        
        # Step 2: Build a balanced BST from the sorted list
        def build_balanced_bst(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            # Create a new node with the middle element as the root
            node = TreeNode(vals[mid]) # type: ignore
            # Recursively build the left and right subtrees
            node.left = build_balanced_bst(left, mid - 1)
            node.right = build_balanced_bst(mid + 1, right)
            return node
        
        return build_balanced_bst(0, len(vals) - 1)
