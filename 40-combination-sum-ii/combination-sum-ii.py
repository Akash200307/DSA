class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res,sol=[],[]

        candidates.sort()
        def dfs(i,sum):
            if sum==target:
                res.append(sol[:])
                return
            if sum> target or i>= len(candidates):
                return
            
            sol.append(candidates[i])
            dfs(i+1,sum+candidates[i])
            sol.pop()

            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,sum)
        dfs(0,0)

        return res

