// Last updated: 2/3/2026, 9:37:29 PM
class Solution {
    public int rangeSum(int[] nums, int n, int left, int right) {
        int[] arr=new int[n * (n + 1) / 2];
        int index=0;
        for(int i=0;i<n;i++){
            int sum=0;
            for(int j=i;j<n;j++){
               sum+=nums[j];
                arr[index++]=sum;
            }
           
        }
        int mod = 1000000007;
        Arrays.sort(arr);
        int sum=0;
        for(int i=left-1;i<right;i++){
            sum=(sum+arr[i])%mod;
        }
        return (int) sum;
    }
   
}