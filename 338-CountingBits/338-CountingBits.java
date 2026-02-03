// Last updated: 2/3/2026, 9:39:22 PM
class Solution {
    public int[] countBits(int n) {
        int[] ans=new int[n+1];
        for(int i=0;i<=n;++i){
            int bit=findonebits(i);
            ans[i]=bit;
        }
        return ans;
    }
    static int findonebits(int n){
        int res=0;
        for(int i=0;i<32;i++){
                if(((n>>i)&1)==1){
                    res++;
                }
        }
        return res;
    }
}