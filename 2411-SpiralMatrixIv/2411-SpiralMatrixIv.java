// Last updated: 2/3/2026, 9:36:32 PM
/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[][] spiralMatrix(int m, int n, ListNode head) {
        int[][] ans = new int[m][n];
        for (int i = 0; i < m; i++) {
            Arrays.fill(ans[i], -1);
        }
        int t = 0,
                b = m - 1,
                l = 0,
                r = n - 1;
        while (head != null) {
            for(int col=l;col<=r&&head!=null;col++){
                ans[t][col]=head.val;
                head =head.next;
            }
            t++;
            for(int row=t;row<=b&&head!=null;row++){
                ans[row][r]=head.val;
                head=head.next;
            }
            r--;
            for(int col=r;col>=l&&head!=null;col--){
                ans[b][col]=head.val;
                head=head.next;
            }
            b--;
            for(int row=b;row>=t&&head!=null;row--){
                ans[row][l]=head.val;
                head=head.next;
            }
            l++;

        }
        return ans;
    }
}