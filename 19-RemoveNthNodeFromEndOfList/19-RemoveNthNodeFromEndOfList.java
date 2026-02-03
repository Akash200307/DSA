// Last updated: 2/3/2026, 9:44:17 PM
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy=new ListNode(0,head);
        ListNode right=head;
        ListNode left=dummy;

        while(n>0){
            right=right.next;
            n=n-1;
        }


        while(right!=null){
            left=left.next;
            right=right.next;
        }
        left.next=left.next.next;
        return dummy.next;
    }
}