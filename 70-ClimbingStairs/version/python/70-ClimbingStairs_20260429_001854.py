# Last updated: 4/29/2026, 12:18:54 AM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        dp=[-1]*(n+1)
4        def dfs(i):
5            if i==n:
6                return 1
7            if i>n:
8                return 0
9            if dp[i]!=-1:
10                return dp[i]
11            dp[i]=dfs(i+1)+dfs(i+2)
12            return dp[i]
13        return dfs(0)