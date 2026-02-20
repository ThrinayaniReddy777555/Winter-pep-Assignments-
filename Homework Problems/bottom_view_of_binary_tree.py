from collections import deque

class TreeNode:
    """Definition for a binary tree node."""
    # def __init__(self, val=0, left=None, right=None):
    #     self.val = val
    #     self.left = left
    #     self.right = right

def bottomView(root: TreeNode) -> list[int]:
    """
    Returns the bottom view of the binary tree from left to right.
    """
    if not root:
        return []
    hd_map = {}
    queue = deque([(root, 0)])
    while queue:
        current_node, hd = queue.popleft()
        hd_map[hd] = current_node.data
        if current_node.left:
            queue.append((current_node.left, hd - 1))
        if current_node.right:
            queue.append((current_node.right, hd + 1))
    sorted_items = sorted(hd_map.items())
    bottom_view_nodes = [item[1] for item in sorted_items]
    return bottom_view_nodes

