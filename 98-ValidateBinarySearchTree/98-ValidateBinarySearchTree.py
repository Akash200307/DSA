# Last updated: 2/3/2026, 9:42:31 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        lst=[]
        self.Inorder(root,lst)
        for i in range(1,len(lst)):
            if lst[i-1]>=lst[i]:
                return False
        return True

    def Inorder(self,node,lst):
        if not node:
            return

        self.Inorder(node.left,lst)
        lst.append(node.val)
        self.Inorder(node.right,lst)