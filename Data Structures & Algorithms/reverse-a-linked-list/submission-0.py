# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        while current!=None:
            temp=current.next
            if current==head:
                current.next=None
            else:
                current.next=prev
            prev=current
            if temp==None:
                head=prev
            current=temp
            

            
            

        
        
        return head
            

        