# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None: # type: ignore
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        def build(inStart: int, inEnd: int, postStart: int, postEnd: int) -> TreeNode | None: # type: ignore
            if inStart > inEnd:
                return None
            
            root_val = postorder[postEnd]
            root_in_index = inorder_map[root_val]
            
            left_size = root_in_index - inStart
            
            root = TreeNode(root_val) # type: ignore
            
            root.left = build(inStart, root_in_index - 1, postStart, postStart + left_size - 1)
            root.right = build(root_in_index + 1, inEnd, postStart + left_size, postEnd - 1)
            
            return root
        
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
