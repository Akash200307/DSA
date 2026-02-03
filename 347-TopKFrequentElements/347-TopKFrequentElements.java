// Last updated: 2/3/2026, 9:39:27 PM
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> map=new HashMap<>();
        int[] res=new int[k];
        for(int i:nums){
            map.put(i,map.getOrDefault(i,0)+1);
        }
     PriorityQueue<Integer> q1=new PriorityQueue<>((a,b)->map.get(b)-map.get(a));
     for(int i:map.keySet()){
        q1.add(i);
     }
     for(int i=0;i<k;i++){
        res[i]=q1.poll();
     }
     return res;
    }
}