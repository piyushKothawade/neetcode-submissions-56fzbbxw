# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        temp = root
        def getHeight(root):
            if not root:
                return -1

            nonlocal diameter

            heightL = getHeight(root.left)
            heightR = getHeight(root.right)

            diameter = max(diameter, heightL + heightR + 2)
            return max(heightL, heightR) + 1
        getHeight(temp)
        return diameter

            