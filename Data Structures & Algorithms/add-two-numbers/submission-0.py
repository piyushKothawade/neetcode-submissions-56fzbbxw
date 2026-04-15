# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        lOld = None
        res = lOld
        while l1 or l2 or carry:
            # I will have the pointer to the prev node already, no need to set it here
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            if carry:
                total += carry
            # node value
            value = total%10
            # carry
            carry = total // 10
            lNew = ListNode(value)
            if lOld:
                lOld.next = lNew
                lOld = lNew
            else:
                res = lNew
                lOld = lNew
        return res
            

