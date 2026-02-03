// Last updated: 2/3/2026, 9:38:37 PM
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
    public ListNode[] splitListToParts(ListNode head, int k) {
        ListNode current=head;
        ListNode[] ans=new ListNode[k];
        int size=0;
        while(current!=null){
            size++;
            current=current.next;
        }
        int eachSize=size/k;
        int ExtraSize=size%k;
        current=head;
        ListNode prev=current;
        for(int i=0;i<k;i++){
            ListNode newPart=current;
            int currsize=eachSize;
            if(ExtraSize>0){
                ExtraSize--;
                currsize++;
            }
            int j=0;
            while(j<currsize){
                prev=current;
                current=current.next;
                j++;
            }
            if(prev!=null){
                prev.next=null;
            }
            ans[i]=newPart;
        }
        return ans;

    }
}