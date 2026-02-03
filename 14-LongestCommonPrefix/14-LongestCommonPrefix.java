// Last updated: 2/3/2026, 9:44:44 PM
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length==0)
         return "";
         String prefix=strs[0];
         for(int i=0;i<strs.length;i++){
             while(strs[i].indexOf(prefix)!=0){
                 prefix=prefix.substring(0,prefix.length()-1);
             }
         }return prefix;
    }
}