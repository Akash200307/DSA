// Last updated: 2/3/2026, 9:40:30 PM
class Solution {
    public boolean isHappy(int n) {
        if(n==1 || n==-1){
            return true;
        }
        HashSet<Integer> s1=new HashSet<>();

        while(!s1.contains(n)){
            s1.add(n);
            n=sumOfSquares(n);
            if(n==1) {
             return true;
            }
        }
        return false;
    }
       public int sumOfSquares(int n){
            int value=0;
            while(n!=0){
                int digit =n%10;
                digit=digit*digit;
                value+=digit;
                n=n/10;
            }
            return value;
        }
    }
    
