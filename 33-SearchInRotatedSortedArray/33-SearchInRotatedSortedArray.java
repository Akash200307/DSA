// Last updated: 2/3/2026, 9:43:50 PM
class Solution {
    public int search(int[] nums, int target) {
        return findvalue(nums,target,0,nums.length-1);
    }
    static int findvalue(int[] arr,int target,int start,int end){
         
        if(start>end){
            return-1;
        }
        int mid=start+(end-start)/2;
        if(arr[mid]==target){
            return mid;
        }
       
      if (arr[start] <= arr[mid]) {
            // Check if the target lies within the sorted left half
            if (arr[start] <= target && target < arr[mid]) {
                return findvalue(arr, target, start, mid - 1);
            } else {
                return findvalue(arr, target, mid + 1, end);
            }
        } 

        // If the right half is sorted
        if (arr[mid] < target && target <= arr[end]) {
            return findvalue(arr, target, mid + 1, end);
        } else {
            return findvalue(arr, target, start, mid - 1);
        }
    }
}