// Last updated: 2/3/2026, 9:39:01 PM
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
    private int maxD=0;
    public int diameterOfBinaryTree(TreeNode root) {

        calculateH(root);

        return maxD;
        
        
    }
    private int calculateH(TreeNode root){

        if(root==null) return 0;

            int left=calculateH(root.left);
            int right=calculateH(root.right);
            maxD=Math.max(maxD,left+right);
            return 1+Math.max(left,right);
        }

}