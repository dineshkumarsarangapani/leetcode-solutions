# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def visit(node, li):
            if node:
                visit(node.left, li)
                li.append(node.val)
                visit(node.right, li)

        a = []
        visit(root, a)
        return a