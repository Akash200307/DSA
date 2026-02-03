// Last updated: 2/3/2026, 9:42:10 PM
class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> h1=new HashSet();
        if(nums.length==0) return 0;
        for(int num:nums) h1.add(num);
        int max=1;
        for(int num:nums){
            if(!h1.contains(num-1)){
                int count=1;
                while(h1.contains(num+1)){
                    num++;
                    count++;
                }
                max=Math.max(max,count);
            }
        }
        return max;
    }
}