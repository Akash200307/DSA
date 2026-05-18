# Last updated: 5/18/2026, 11:42:38 PM
1class Solution:
2    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
3        if not head:
4            return None
5
6        tail = head
7
8        for _ in range(k):
9            if not tail:
10                return head
11            tail = tail.next
12
13        def reverse(cur, end):
14            prev = None
15
16            while cur != end:
17                next = cur.next
18                cur.next = prev
19                prev = cur
20                cur = next
21
22            return prev      
23
24        new_head = reverse(head, tail)
25        head.next = self.reverseKGroup(tail, k)
26
27        return new_head            