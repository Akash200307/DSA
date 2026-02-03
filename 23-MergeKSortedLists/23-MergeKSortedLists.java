// Last updated: 2/3/2026, 9:43:55 PM
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
    public ListNode mergeKLists(ListNode[] lists) {

        if(lists.length<1){
            return null;
        }
        
        PriorityQueue<ListNode> minh=new PriorityQueue<>((a,b)->a.val -b.val);

        for(ListNode i:lists){
            if(i!=null){
                minh.add(i);
            }
        }
        ListNode res=new ListNode();
        ListNode dummy=res;

        while(!minh.isEmpty()){
            ListNode node = minh.poll();
            dummy.next=node;
            dummy=dummy.next;
            node=node.next;
            if(node!=null){
                minh.add(node);
            }
        }
        return res.next;

    }
}