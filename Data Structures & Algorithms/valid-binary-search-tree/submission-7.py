# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, [-1001, 1001])])

        while len(queue):
            # till now, it's a valid BST
            for i in range(len(queue)):
                grp = queue.popleft()
                node = grp[0]
                limit = grp[1]
                # first check if it's children are within the limits
                if node.left:
                    if not (limit[0] < node.left.val and node.left.val < node.val):
                        print(limit)
                        return False
                    queue.append((node.left, [limit[0], node.val]))
                if node.right:
                    if not (node.val < node.right.val and node.right.val < limit[1]):
                        print(limit)
                        return False
                    queue.append((node.right, [node.val, limit[1]]))
        return True


