// Last updated: 2/3/2026, 9:36:56 PM
class Solution {
    public int getLucky(String s, int k) {
        StringBuilder str=new StringBuilder();
        for(char i:s.toCharArray()){
            str.append(i-'a'+1);
        }
        while(k>0){
            int temp=0;
            for(char i:str.toString().toCharArray()){
                temp+=i-'0';
            }
            str=new StringBuilder(String.valueOf(temp));
            k--;
        }
        return  Integer.parseInt(str.toString());
    }

}