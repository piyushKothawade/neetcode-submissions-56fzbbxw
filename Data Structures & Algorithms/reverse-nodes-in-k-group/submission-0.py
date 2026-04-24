# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nextCurr = curr.next
            curr.next = prev
            prev = curr
            curr = nextCurr
        return prev
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # HEAD, PREV
        # REVERSE K NODES STARTING FROM HEAD
        # PREV.NEXT = NEW_HEAD
        # OLD_HEAD BECOMES THE NEW PREV
        # OLD_HEAD.NEXT BECOMES THE NEW HEAD
        prev = ListNode(-1)
        MAIN = prev
        prev.next = head
        temp = head
        while 1:
            # reverse k nodes starting from temp
            sp = 0
            rp = None
            curr = temp
            while sp != k and curr:
                rn = curr.next
                curr.next = rp
                rp = curr
                curr = rn
                sp += 1
                print(sp)
            if sp != k:
                newHead = self.reverseList(rp)
                prev.next = newHead
                break
            prev.next = rp
            prev = temp
            temp = curr
        return MAIN.next



