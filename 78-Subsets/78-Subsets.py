# Last updated: 2/3/2026, 9:42:54 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sol=[]
        n=len(nums)
        def dfs(i):
            if i==n:
                res.append(sol.copy())
                return
            sol.append(nums[i])
            dfs(i+1)
            sol.pop()
            dfs(i+1)
        dfs(0)
        return res