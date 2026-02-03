// Last updated: 2/3/2026, 9:39:38 PM
class Solution {
    public int findDuplicate(int[] nums) {


        if(nums.length==0) return 0;

        int slow=0;
        int fast =0;
        while(true){
            slow=nums[slow];
            fast= nums[nums[fast]];
            if(slow==fast){
                break;
            }
        }

            int sno=0;
            while(true){
                sno=nums[sno];
                fast=nums[fast];
                if(sno==fast){
                    return sno;
                }

            }

    }
}