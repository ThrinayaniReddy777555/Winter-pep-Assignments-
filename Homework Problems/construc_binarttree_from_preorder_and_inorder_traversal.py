# Definition for a binary tree node.
'''class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right'''

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None: # type: ignore
        inorder_map = {val: i for i, val in enumerate(inorder)}

        def build(pre_start: int, pre_end: int, in_start: int, in_end: int) -> TreeNode | None: # type: ignore
            if pre_start > pre_end or in_start > in_end:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val) # type: ignore

            root_in_index = inorder_map[root_val]
            left_size = root_in_index - in_start

           
            root.left = build(pre_start + 1, pre_start + left_size, in_start, root_in_index - 1)

           
            root.right = build(pre_start + left_size + 1, pre_end, root_in_index + 1, in_end)

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

