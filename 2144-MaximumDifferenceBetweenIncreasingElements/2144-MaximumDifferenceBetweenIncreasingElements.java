// Last updated: 2/3/2026, 9:36:50 PM
import java.util.*;
class Solution {
    public int maximumDifference(int[] nums) {
        int l=0;
        int max=-1;
        int r=1;
       while(r<nums.length){
        if(nums[l]<nums[r]){
            int currdiff=nums[r]-nums[l];
            max=Math.max(max,currdiff);
        }else{
            l=r;
        }
        r++;
       }
       return max;
    }
}