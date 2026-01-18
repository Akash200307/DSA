# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        nodes_list=[]
        curr=head
        while curr:
            nodes_list.append(curr.val)
            curr=curr.next
        
        return nodes_list==nodes_list[::-1]
        