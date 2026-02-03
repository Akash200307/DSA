// Last updated: 2/3/2026, 9:39:58 PM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {

        TreeNode curr=root;

        while(curr!=null){
            if(p.val<curr.val && q.val <curr.val){
                curr=curr.left;
            }
            else if(p.val>curr.val && q.val >curr.val){
                curr=curr.right;
            }
            else{
                return curr;
            }
        }

        return null;
        
    }
}