// Last updated: 2/3/2026, 9:38:22 PM
class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l=1;
        int r=Arrays.stream(piles).max().getAsInt();
        int res=r;
        while(l<=r){
            int mid=(l+r)/2;
            int Time=0;
            for(int i :piles){
                Time+=Math.ceil((double)i/mid);
            }
            if (Time<=h){
                res=mid;
                r=mid-1;
            }
            else{
                l=mid+1;
            }
        }
        return res;
    }
}