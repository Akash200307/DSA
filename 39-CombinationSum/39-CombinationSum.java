// Last updated: 2/3/2026, 9:43:36 PM
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(0, candidates, new ArrayList<>(), 0, res, target);
        return res;
    }

    void dfs(int i, int[] cdd, List<Integer> cur, int totalSoFar, List<List<Integer>> res, int target){
        if(totalSoFar == target){
            res.add(new ArrayList<>(cur));
            return;
        }
        if(i>=cdd.length || totalSoFar>target){
            return;
        }
        // take this candidate element
        cur.add(cdd[i]);
        dfs(i, cdd, cur, totalSoFar + cdd[i], res, target);
        cur.remove(cur.size()-1);
        // do not take this candidate element
        dfs(i+1, cdd, cur, totalSoFar, res, target);
    }
}