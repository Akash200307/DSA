// Last updated: 2/3/2026, 9:40:49 PM
class Solution {
    public int majorityElement(int[] nums) {
        int count=0;
        int element=0;
        int n=nums.length;
        for(int i=0;i<n;i++){
            if(count==0){
                count=1;
                element=nums[i];
            }
            else if(element==nums[i]){
                count++;
            }
            else{
                count--;
            }
        }
        int temp=0;
    for(int i=0;i<n;i++){
        if(nums[i]==element){
            temp++;
        }
    }
    if(temp>n/2){
        return element;
    }
    else
      return -1;
}
}