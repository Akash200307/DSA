// Last updated: 2/3/2026, 9:39:15 PM
class Solution {
    public int characterReplacement(String s, int k) {

        HashMap<Character,Integer> freq=new HashMap<>();
        int max_f=0;
        int l=0;

        for (int r=0;r<s.length();r++){
            char curr= s.charAt(r);
            freq.put(curr,1+freq.getOrDefault(curr,0));
            max_f=Math.max(freq.get(curr),max_f);

            if(((r-l)+1 -max_f)>k ){
                
                freq.put(s.charAt(l),freq.get(s.charAt(l))-1);
                l+=1;
            }
        }

        return s.length()-l;
        
    }
}