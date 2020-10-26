# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValid(root, lo=float('-inf'), hi=float('inf')):
            """
            :type root: TreeNode
            :rtype: bool
            """
            if not root:
                return True

            if not lo < root.val < hi:
                return False

            return isValid(root.left, lo, min(root.val, hi)) and \
                   isValid(root.right, max(lo, root.val), hi)
        return isValid(root)