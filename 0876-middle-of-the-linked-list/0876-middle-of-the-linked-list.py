# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp=head
        l=0
        while temp:
            l+=1
            temp=temp.next
        curr=head
        l=l//2
        for i in range(l):
            curr=curr.next
        return curr

        