// Last updated: 2/3/2026, 9:36:41 PM
class Solution {
    public String kthDistinct(String[] arr, int k) {
        int i=k;
        HashMap<String,Integer> map=new HashMap();
        for(String s:arr){
            map.put(s,map.getOrDefault(s,0)+1);
        
        }

        for(String s:arr){
            if(map.get(s)==1){
                --i;
                if(i==0){
                    return s;
                }
            }
        }
        return "";
    }
}