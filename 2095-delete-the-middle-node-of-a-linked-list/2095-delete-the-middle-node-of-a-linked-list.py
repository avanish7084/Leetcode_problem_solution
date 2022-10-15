# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        if head.next==None:
            return None
        p=None
        while fast!=None and fast.next!=None:
            p=slow
            fast=fast.next.next
            slow=slow.next
        p.next=slow.next
        return head