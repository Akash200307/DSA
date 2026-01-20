# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

       
    
        def traverse(root,lst):

            if not root:
                return
            
            traverse(root.left,lst)
            traverse(root.right,lst)
            lst.append(root.val)

        lst=[]
        traverse(root,lst)

        lst.sort()

        return lst[k-1]
