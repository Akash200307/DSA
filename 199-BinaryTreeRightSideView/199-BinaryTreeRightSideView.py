# Last updated: 2/3/2026, 9:40:39 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
      q=collections.deque([root])
      q.append(root)
      res=[]

      while q:
        r=None
        l=len(q)
        for _ in range(l):
          node=q.popleft()
          if node:
            r=node
            q.append(node.left)
            q.append(node.right)
        if r:
          res.append(r.val)
      return res
        

        