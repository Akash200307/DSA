class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res,sol=[],[]
        def dfs(i,sum):
            if sum==target:
                res.append(sol[:])
                return
            if sum>target or i>=len(candidates):
               return
            sol.append(candidates[i])
            dfs(i,sum+candidates[i])

            sol.pop()
            dfs(i+1,sum)


        dfs(0,0)
        return res
