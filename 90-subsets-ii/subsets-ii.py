class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res,sol=[],[]
        n=len(nums)
        def dfs(i,curr):
            if i==n:
                res.append(sol.copy())
                return
            sol.append(nums[i])
            dfs(i+1,nums[i])
            sol.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1,nums[i])
        dfs(0,0)

        return res