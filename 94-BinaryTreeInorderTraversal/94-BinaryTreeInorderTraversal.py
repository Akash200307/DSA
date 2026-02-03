# Last updated: 2/3/2026, 9:42:39 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        lst=[]
        self.Inorder(root,lst)
        return lst
    def Inorder(self,node,lst):
        if not node:
            return

        self.Inorder(node.left,lst)
        lst.append(node.val)
        self.Inorder(node.right,lst)