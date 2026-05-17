# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        temp1 = p
        temp2 = q
        def solve(root1, root2):
            # base case
            if (not root1 and root2) or (not root2 and root1):
                return False
            if not root1 and not root2:
                return True

            # assume that both are non-None
            if root1.val != root2.val:
                return False
            
            checkLeft = solve(root1.left, root2.left)
            checkRight = solve(root1.right, root2.right)

            if not (checkLeft and checkRight):
                return False
            
            return True
        return solve(temp1, temp2)
            
