// Last updated: 2/3/2026, 9:43:07 PM
class Solution {
    public int lengthOfLastWord(String s) {
        String [] str =s.split(" ");

        return str[str.length-1].length();
    }
}