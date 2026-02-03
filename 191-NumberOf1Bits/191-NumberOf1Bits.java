// Last updated: 2/3/2026, 9:40:53 PM
class Solution {
    public int hammingWeight(int n) {

        int res=0;
        for(int i=0;i<32;i++){
            if(((n>>i)&1)==1){
                res++;
            }
        }
        return res;
    }
}