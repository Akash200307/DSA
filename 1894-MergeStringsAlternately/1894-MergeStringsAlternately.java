// Last updated: 2/3/2026, 9:37:11 PM
class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder s1=new StringBuilder();
        for(int i=0;
        i<Math.max(word1.length(),word2.length());
        i++){
                if(i<word1.length()){
                    s1.append(word1.charAt(i));
                }
            if(i<word2.length()){
                s1.append(word2.charAt(i));
            }
        }
        return s1.toString();
    }
}