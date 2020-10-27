# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from python.source.tree.tree import TreeNode


def get_tree():
    root = TreeNode()
    root.val = 1
    two = TreeNode()
    two.val = 2
    root.right = two
    three = TreeNode()
    three.val = 3
    two.left = three
    return root


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def visit(node, li):
            if node:
                li.append(node.val)
                visit(node.left, li)
                visit(node.right, li)

        a = []
        visit(root, a)
        return a


if __name__ == '__main__':
    s = Solution()
    y = s.preorderTraversal(get_tree())
    print(y)
