// Last updated: 2/3/2026, 9:43:00 PM
class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        
        // Iterate from the last digit to the first
        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            // If the digit is 9, it becomes 0
            digits[i] = 0;
        }
        
        // If all digits were 9, we need an extra digit at the start
        int[] newNumber = new int[n + 1];
        newNumber[0] = 1;
        
        return newNumber;
    }
}
