// Last updated: 2/3/2026, 9:37:56 PM
class Solution {
    public int largestPerimeter(int[] nums) {
        Arrays.sort(nums);
        for (int i=nums.length-1;i>=2;i--){
            int sides=nums[i-1]+nums[i-2];
            if(nums[i]<sides){
                return sides+nums[i];
            }
        }
        return 0;
    }
}