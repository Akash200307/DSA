// Last updated: 2/3/2026, 9:37:45 PM
class Solution {
    public int subtractProductAndSum(int n) {
        
        int sum = 0, prod = 1;

        while (n != 0) {

            int rightNumber = n % 10;

          
            sum += rightNumber;
            prod *= rightNumber;

           
            n /= 10;
        }

        return prod - sum;
    }
}