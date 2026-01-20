# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        lst=[]
        self.inorder(root,lst)

        for i in range(1,len(lst)):
            if lst[i-1]>=lst[i]:
                return False
        return True

    def inorder(self,node,inorderList):

        if not node:
            return 
        self.inorder(node.left,inorderList)
        inorderList.append(node.val)
        self.inorder(node.right,inorderList)