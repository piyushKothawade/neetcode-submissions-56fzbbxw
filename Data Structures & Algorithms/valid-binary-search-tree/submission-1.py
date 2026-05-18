# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # compute the inorder traversal
        inOrder = []

        def inOrderTraversal(root):
            if not root:
                return

            nonlocal inOrder
            inOrderTraversal(root.left)
            inOrder.append(root.val)
            inOrderTraversal(root.right)

            return
        inOrderTraversal(root)

        for i in range(1, len(inOrder)):
            if inOrder[i] <= inOrder[i-1]:
                return False
        return True