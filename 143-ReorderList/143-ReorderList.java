// Last updated: 2/3/2026, 9:41:38 PM
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
    public void reorderList(ListNode head) {
        
        ListNode slow=head;
        ListNode fast= head.next;

        while(fast!=null && fast.next!=null){
            slow=slow.next;
            fast=fast.next.next;
        }
        ListNode secondH=slow.next;
        ListNode prev=null;
        slow.next=null;

        while(secondH!=null){
            ListNode t= secondH.next;
            secondH.next=prev;
            prev=secondH;
            secondH=t;
        }
        ListNode first=head;
        secondH=prev;
        while(secondH!=null){
            ListNode temp1=first.next;
            ListNode temp2=secondH.next;
            first.next=secondH;
            secondH.next=temp1;
            first=temp1;
            secondH=temp2;
            
        }
    }
}