// Last updated: 2/3/2026, 9:39:54 PM
class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }

        HashMap<Character,Integer> map1=new HashMap<Character,Integer>();
        HashMap<Character,Integer> map2=new HashMap<Character,Integer>();

        for(int i=0;i<s.length();i++){
            map1.put(s.charAt(i),map1.getOrDefault(s.charAt(i),0)+1);
            map2.put(t.charAt(i),map2.getOrDefault(t.charAt(i),0)+1);

        }

        return map1.equals(map2);
    }
}