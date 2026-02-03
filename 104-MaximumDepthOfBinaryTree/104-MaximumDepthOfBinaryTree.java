// Last updated: 2/3/2026, 9:42:34 PM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {

        if(root==null) return 0;

        int MaxLeft=maxDepth(root.left);
        int MaxRight=maxDepth(root.right);


        return 1+Math.max(MaxLeft,MaxRight);
        
    }
}