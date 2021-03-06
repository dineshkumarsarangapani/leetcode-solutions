# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import SimpleQueue
from typing import List

from python.source.tree.tree import TreeNode


def get_tree():
    root = TreeNode()
    root.val = 3
    nine = TreeNode()
    nine.val = 9
    root.left = nine
    twentiy = TreeNode()
    twentiy.val = 20
    root.right = twentiy
    fift = TreeNode()
    fift.val = 15
    seven = TreeNode()
    seven.val = 7
    twentiy.left = fift
    twentiy.right = seven
    return root


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        visited = []
        q = SimpleQueue()
        q.put(root)
        while not q.empty():
            current_level = []
            size = q.qsize()
            for i in range(size):
                node = q.get()
                if node:
                    current_level.append(node.val)
                    if node.left:
                        q.put(node.left)
                    if node.right:
                        q.put(node.right)

            visited.append(current_level)

        return visited


if __name__ == '__main__':
    s = Solution()
    y = s.levelOrder(get_tree())
    print(y)
