// Last updated: 2/3/2026, 9:40:42 PM
class Solution {
    public void rotate(int[] nums, int k) {
       int n=nums.length;
    k=k%n;
    int [] rotate=new int [n];
    for(int i=0;i<n;i++){
        rotate[(i+k)%n]=nums[i];
    }
    int r=0;
    for(int i:rotate){
        nums[r]=i;
        r++;
    }
    }
    
}