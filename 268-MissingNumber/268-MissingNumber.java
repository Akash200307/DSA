// Last updated: 2/3/2026, 9:39:45 PM
class Solution {
    public int missingNumber(int[] nums) {
        int sum=Arrays.stream(nums).sum();
        int n=nums.length;
        int cal=n*(n+1)/2;
        int result=cal-sum;
      return result;
    }
}