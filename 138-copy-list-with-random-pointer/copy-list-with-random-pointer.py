"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        copy_old={None:None}
        curr=head
        while curr:
            copy=Node(curr.val)
            copy_old[curr]=copy
            curr=curr.next
        
        curr=head

        while curr:
            copy=copy_old[curr]
            copy.next=copy_old[curr.next]
            copy.random=copy_old[curr.random]
            curr=curr.next

        return copy_old[head]



        