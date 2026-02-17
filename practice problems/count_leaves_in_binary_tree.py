class Solution:
    def countLeaves(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return self.countLeaves(root.left) + self.countLeaves(root.right)
       

