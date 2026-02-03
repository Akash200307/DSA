# Last updated: 2/3/2026, 9:40:25 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev=None
        curr=head

        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev

        