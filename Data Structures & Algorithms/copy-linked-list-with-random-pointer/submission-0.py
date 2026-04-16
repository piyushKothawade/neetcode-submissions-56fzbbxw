"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        corr = dict()
        corr[None] = None
        temp = head
        # need the prev already
        prev = None
        res = None
        while temp:
            print(temp.val)
            # we need to check if the copy of temp has already been created in 'corr'
            corrTemp = None
            if temp in corr:
                corrTemp = corr[temp]
            else:
                corrTemp = Node(temp.val)
                corr[temp] = corrTemp
            # Have the copy of temp now
            # *****NEXT****
            # join it to the copied linked list
            if prev:
                prev.next = corrTemp
            else:
                res = corrTemp
            # *****RANDOM*****
            randomNode = temp.random
            if randomNode in corr:
                corrTemp.random = corr[randomNode]
            else:
                # make a new random Node
                corrRandom = Node(randomNode.val)
                corr[randomNode] = corrRandom
                corrTemp.random = corrRandom
            prev = corrTemp
            temp = temp.next
        return res