# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        queue = deque()

        queue.append(root)
        while len(queue):
            # curr queue has all the nodes in the current level
            currList = []
            currLen = len(queue)
            for i in range(currLen):
                currList.append(queue[0].val)
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                queue.popleft()
            res.append(currList)
        return res
                
