# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def visit(node, li):
            if node:
                visit(node.left, li)
                visit(node.right, li)
                li.append(node.val)

        a = []
        visit(root, a)
        return a