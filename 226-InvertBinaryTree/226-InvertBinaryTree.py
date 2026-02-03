# Last updated: 2/3/2026, 9:40:10 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        temp=root.right
        root.right=root.left
        root.left=temp

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root