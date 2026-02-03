# Last updated: 2/3/2026, 9:43:26 PM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res=[]
        sol=[]

        def dfs(i,sum):
            if sum==target:
                res.append(sol.copy())
                return
            if sum>target or i>=len(candidates):
                return
            
            sol.append(candidates[i])
            dfs(i,sum+candidates[i])
            sol.pop()
            dfs(i+1,sum)
        dfs(0,0)
        return res