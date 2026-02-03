// Last updated: 2/3/2026, 9:40:32 PM
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<Integer>();
        for (int i:nums){
            if (set.contains(i)){
                return true;
            }
            set.add(i);
        }
        return false;
        
    }
}