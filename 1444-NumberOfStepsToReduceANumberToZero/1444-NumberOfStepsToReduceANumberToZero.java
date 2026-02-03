// Last updated: 2/3/2026, 9:37:42 PM
class Solution {
    public int numberOfSteps(int num) {
        return steps(num,0);
    }
    static int steps(int n,int c ){
            if(n==0){
                return c;
            }
            if(n%2==0){
                
                return steps(n/2,c+1);
            }
            else{
                return steps(n-1,c+1);
            }

    }
}