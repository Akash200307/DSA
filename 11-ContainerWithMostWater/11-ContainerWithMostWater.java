// Last updated: 2/3/2026, 9:44:48 PM
class Solution {
    public int maxArea(int[] height) {

        int maxW=0;
        int l=0;
        int r=height.length-1;
        while(l<r){
            int area=Math.min(height[l],height[r])*(r-l);
            maxW=Math.max(maxW,area);
            if(height[l]<=height[r]){
                l++;
            }
            else{
                r--;
            }
        }
        return maxW;
    }
}