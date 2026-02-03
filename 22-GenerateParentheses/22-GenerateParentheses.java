// Last updated: 2/3/2026, 9:44:03 PM
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> list =new ArrayList<>();
        backtrack(list,0,0,"",n);
        return list;

    }
    static void backtrack(List<String> res,int open,int close,String curr,int n){
        if(curr.length()==n*2){
            res.add(curr);
            return;
        }
        if(open <n) backtrack(res,open+1,close,curr+"(",n);
        if(open>close) backtrack(res,open,close+1,curr+")",n);
    }
}