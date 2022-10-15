# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        """
        slow=fast=head
        if head==None:
            return []
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
      
        curr=slow.next
        prev=nextt=None
        while curr:
            nextt=curr.next
            curr.next=prev
            prev=curr
            curr=nextt
        
        slow.next=None
        
        
        temp=None
        h1,h2=head,prev
        while h2:
            temp=h1.next
            h1.next=h2
            h1=h2
            h2=temp
         
        