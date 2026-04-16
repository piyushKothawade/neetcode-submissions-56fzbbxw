# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, head1, head2):
        HEAD = ListNode(0)
        temp = HEAD
        while head1 or head2:
            if head1 and head2:
                if head1.val <= head2.val:
                    temp.next = head1
                    temp = head1
                    head1 = head1.next
                else:
                    temp.next = head2
                    temp = head2
                    head2 = head2.next
            elif not head1:
                temp.next = head2
                return HEAD.next
            else:
                temp.next = head1
                return HEAD.next
        return None


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not len(lists):
            return None
        t2 = lists[0]
        for head in lists[1:]:
            # head is t1
            t1 = head
            t2 = self.merge(t1,t2)
        return t2

