# Last updated: 2/3/2026, 9:37:37 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

      def dfs(node,maxV):
        if not node:
          return 0
        
        if node.val>=maxV:
          res=1
        else:
          res=0
        maxV=max(maxV,node.val)
        res+=dfs(node.left,maxV)+dfs(node.right,maxV)
        
        return res
      return dfs(root,root.val)
        

        