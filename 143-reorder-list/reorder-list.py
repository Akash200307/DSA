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
        dup_list=[]
        curr=head
        while curr:
            dup_list.append(curr.val)
            curr=curr.next

        curr = head
        curr.next = None

        left=1
        right=len(dup_list)-1

        while(left<=right):
            curr.next = ListNode(dup_list[right])
            curr = curr.next
            right -= 1
            
            # If we still have elements from left side
            if left <= right:
                curr.next = ListNode(dup_list[left])
                curr = curr.next
                left += 1

           

        