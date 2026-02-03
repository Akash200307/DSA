// Last updated: 2/3/2026, 9:41:58 PM
class Solution {
    public int singleNumber(int[] nums) {
        int n=nums.length;
        int xrr=0;
        for(int i=0;i<n;i++){
            xrr=xrr^nums[i];
        }
        return xrr;

    }
}