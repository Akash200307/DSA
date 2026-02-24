# Last updated: 2/24/2026, 8:23:14 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
9        
10        res=[]
11        sol=""
12        def dfs(node,sol):
13            if not node:
14                return 0
15
16            sol+=str(node.val)
17
18            if not node.left and not node.right:
19                res.append(sol)
20                return
21            
22            dfs(node.left,sol)
23            dfs(node.right,sol)
24        
25        dfs(root,"")
26
27        num=0
28        for i in res:
29            num+=int(i,2)
30        
31
32        return num
33
34
35
36
37