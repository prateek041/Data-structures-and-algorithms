from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)

    def dfs (self, root: Optional[TreeNode], height: int) -> int:
        if not root:
            return height
        height += 1
        left_height = self.dfs(root.left, height)
        right_height = self.dfs(root.right, height)
        return max(left_height, right_height)
