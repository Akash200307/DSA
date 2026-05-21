# Last updated: 5/21/2026, 7:16:56 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        temp=ListNode()
9        curr=temp
10        carry=0
11        while l1 or l2 or carry:
12            
13            v1=l1.val if l1 else 0
14            v2=l2.val if l2 else 0
15
16            val=v1+v2+carry
17            carry=val//10
18            val=val%10
19
20            curr.next=ListNode(val)
21
22            curr=curr.next
23
24            l1=l1.next if l1 else None
25            l2=l2.next if l2 else None
26
27        return temp.next