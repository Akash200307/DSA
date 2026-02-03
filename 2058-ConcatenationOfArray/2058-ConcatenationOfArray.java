// Last updated: 2/3/2026, 9:37:09 PM
class Solution {
    public int[] getConcatenation(int[] nums) {
         int[] n=new int[nums.length*2];
        for(int i=0;i<nums.length*2;i++){
        if(i<nums.length){
           n[i]=nums[i];
        }
        else{
            n[i]=nums[i-nums.length];
        }
        
    }
return n;
    }
}