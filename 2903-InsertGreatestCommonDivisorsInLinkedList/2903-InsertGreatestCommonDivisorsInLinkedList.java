// Last updated: 2/3/2026, 9:36:10 PM
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
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        if(head==null) return head;
        ListNode node1= head;
        ListNode node2=head.next;

        while(node2!=null){
            int Gcd=gcd(node1.val,node2.val);
            ListNode NodeGcd=new ListNode(Gcd);

            node1.next=NodeGcd;
            NodeGcd.next=node2;
           
            node1=node2;
            node2=node1.next;

        }
         return head;
    }

        private  int gcd(int a,int b){
            while(b!=0){
                int temp=b;
                b=a%b;
                a=temp;
            }
            return a;
        }
}
    
