// Last updated: 2/3/2026, 9:43:24 PM
import java.math.*;
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if(strs.length==0||strs==null){
            return null;
        }
        Map<BigInteger,List<String>> m1=new HashMap<>();
        int[] EcAssign={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,97,101,103};
                for (String word : strs) {
            BigInteger prod = BigInteger.ONE; // Use BigInteger.ONE for efficiency
            for (char c : word.toCharArray()) {
                int index = c - 'a'; // Efficient char to index conversion
                prod = prod.multiply(BigInteger.valueOf(EcAssign[index]));
            }

            if(m1.containsKey(prod)){
                m1.get(prod).add(word);
            }
            else{
                m1.put(prod,new ArrayList<String>());
                m1.get(prod).add(word);
            }
        }
         List<List<String>> l1=new ArrayList<>();
         for(List<String> s1:m1.values()){
            l1.add(s1);
         }
            return l1;
    }
}