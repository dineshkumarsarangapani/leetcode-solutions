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

        visited = []
        visit(root, visited)
        return visited


class LoopSolution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        li =[]
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                li.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return li


if __name__ == '__main__':
    s = LoopSolution()
    y = s.preorderTraversal(get_tree())
    print(y)
