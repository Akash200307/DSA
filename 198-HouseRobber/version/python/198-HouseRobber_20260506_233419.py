# Last updated: 5/6/2026, 11:34:19 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        dp=[-1]*(len(nums))
4        def dfs(i):
5            if i>=len(nums):
6                return 0
7            if dp[i]!=-1:
8                return dp[i]
9            dp[i]=max(dfs(i+1),nums[i]+dfs(i+2))
10            return dp[i]
11        return dfs(0)
12
13
14        