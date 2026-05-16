# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        temp = root
        res = True
        def getHeight(temp):
            if not temp:
                return -1

            nonlocal res
            heightL = getHeight(temp.left)
            heightR = getHeight(temp.right)

            if abs(heightL - heightR) > 1:
                res = False
            return max(heightL, heightR) + 1
        getHeight(temp)
        return res