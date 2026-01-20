# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        lst=[]

        self.preorder(root,lst)

        return lst


    def preorder(self,root,lst):

        if not root:
            return
        
        lst.append(root.val)
        self.preorder(root.left,lst)
        self.preorder(root.right,lst)

        