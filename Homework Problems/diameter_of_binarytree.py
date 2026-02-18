class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:#type: ignore 
        ans = 0

        def maxDepth(root: TreeNode | None) -> int:#type: ignore 
            nonlocal ans
            if not root:
                return 0
            l = maxDepth(root.left)
            r = maxDepth(root.right)
            ans = max(ans, l + r)
            return 1 + max(l, r)

        maxDepth(root)
        return ans
