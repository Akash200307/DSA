// Last updated: 2/3/2026, 9:44:52 PM
class Solution {
    public int reverse(int x) {
       int num=Math.abs(x);
       int rev=0;
       while(num!=0){
        int last=num%10;
        if(rev>(Integer.MAX_VALUE-last)/10){
            return 0;
        }
        rev=(rev*10)+last;
        num=num/10;
       }
       return (x<0)? (-rev):rev;
    }
}