# Definition for a binary tree node.
from python.source.tree.tree import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root is not None else 0




