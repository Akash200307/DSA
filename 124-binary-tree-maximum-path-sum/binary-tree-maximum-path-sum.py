# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=root.val

        def dfs(node):
            nonlocal res

            if not node:
                return 0

            left=dfs(node.left)
            left=0 if left<0 else left

            right=dfs(node.right)
            right=0 if right<0 else right

            res=max(res,right+left+node.val)

            return node.val+max(left,right)
        dfs(root)

        return res
        