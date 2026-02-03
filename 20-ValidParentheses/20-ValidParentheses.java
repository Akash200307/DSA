// Last updated: 2/3/2026, 9:44:14 PM
class Solution {
    public boolean isValid(String s) {
       Stack<Character> s1=new Stack();
       HashMap<Character,Character> map=new HashMap<>();
       map.put('}','{');
       map.put(']','[');
       map.put(')','(');
    char[] arr=s.toCharArray();
        for(char i:arr){
            if(s1.isEmpty()){
                s1.push(i);
            }
            else if(s1.peek()==map.get(i)){
                s1.pop();
            }
            else{
                s1.push(i);
            }
        }
        return s1.isEmpty();
        
    }
}
