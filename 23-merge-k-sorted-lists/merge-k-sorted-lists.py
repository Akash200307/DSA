# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        if not lists:
            return None

        nodes=[]

        for lst in lists:
            while lst:
                nodes.append(lst.val)
                lst=lst.next
        nodes.sort()


        res=ListNode(0)
        st=res

        for node in nodes:
            st.next=ListNode(node)
            st=st.next

        return res.next

        