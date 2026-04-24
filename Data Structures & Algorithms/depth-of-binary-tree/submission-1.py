# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if not root:
                return 0
            if root.left == None and root.right == None:
                return 1

            leftDepth = solve(root.left)
            rightDepth = solve(root.right)

            return 1 + max(leftDepth, rightDepth)
        return solve(root)