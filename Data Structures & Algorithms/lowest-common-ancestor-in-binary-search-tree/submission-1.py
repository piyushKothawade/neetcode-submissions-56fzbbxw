# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        temp = root
        while temp:
            print(temp.val)
            if min(p.val, q.val) < temp.val and max(p.val, q.val) > temp.val:
                return temp
            if p.val == temp.val or q.val == temp.val:
                return temp
            
            # Either both are small
            if max(p.val, q.val) < temp.val:
                temp = temp.left
            else:
                temp = temp.right
        return root