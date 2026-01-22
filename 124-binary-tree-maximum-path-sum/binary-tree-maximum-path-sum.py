# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res=[root.val]

        def maxDown(node):
            if not node:
                return 0
            

            left_s=maxDown(node.left)
            right_s=maxDown(node.right)
            left_m=max(0,left_s)
            right_m=max(0,right_s)
            res[0]=max(res[0],left_m+right_m+node.val)
            return node.val+max(left_m,right_m)
        
        maxDown(root)
        return res[0]