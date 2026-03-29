# Last updated: 3/29/2026, 10:20:34 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        res=float("-inf")
10        def dfs(node):
11            nonlocal res
12            if not node:
13                return 0
14
15            left=dfs(node.left)
16            left=0 if left<0 else left
17            right=dfs(node.right)
18            right=0 if right<0 else right
19            res=max(res,node.val+left+right)
20            return node.val+max(left,right)
21        dfs(root)
22        return res