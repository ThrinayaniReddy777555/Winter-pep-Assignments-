class Solution:
    def height(self, root):
        if root is None:
            return -1
        left_h = self.height(root.left)
        right_h = self.height(root.right)
        return 1 + max(left_h, right_h)