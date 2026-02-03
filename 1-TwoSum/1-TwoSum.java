// Last updated: 2/3/2026, 9:45:01 PM
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer>  h1 = new HashMap<>();
        for (int i=0; i<nums.length;i++){
            int num = nums[i];
            if(h1.containsKey(target-num)){
                return new int[] {h1.get(target-num),i};
            }

            h1.put(num,i);
        }
        return new int[]{};
        
    }
}