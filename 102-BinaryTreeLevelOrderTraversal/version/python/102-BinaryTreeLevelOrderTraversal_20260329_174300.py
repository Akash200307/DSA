# Last updated: 3/29/2026, 5:43:00 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution:
9    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
10        if not root:
11            return []
12        queue = deque([root])
13        res=[]
14        while queue:
15            q_len=len(queue)
16            level=[]
17            for _ in range(q_len):
18                node=queue.popleft()
19                level.append(node.val)
20                if node.left:
21                    queue.append(node.left)
22                if node.right:
23                    queue.append(node.right)
24            
25            res.append(level)
26        return res