class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res=[]
        sol=[]

        def dfs(i,curr,sum):
            if sum==target:
                res.append(sol.copy())
                return
            if sum>target or i>=len(candidates):
                return
            
            sol.append(candidates[i])
            dfs(i+1,candidates[i],sum+candidates[i])
            sol.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]  :
                i+=1
            dfs(i+1,candidates[i],sum)

        dfs(0,0,0)
        return res

