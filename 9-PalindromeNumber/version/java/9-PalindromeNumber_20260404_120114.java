// Last updated: 4/4/2026, 12:01:14 PM
1class Solution {
2    public boolean isPalindrome(int x) {
3        if (x<0){
4            return false;
5        }
6        StringBuilder x1= new StringBuilder(Integer.toString(x));
7        return x1.toString().equals(x1.reverse().toString());
8    }
9}