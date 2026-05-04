# Last updated: 5/4/2026, 6:19:55 AM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        dp=[-1]*(len(cost))
4        def dfs(i):
5            if i>=len(cost):
6                return 0
7            
8            if dp[i]!=-1:
9                return dp[i]
10            dp[i]=cost[i]+min(dfs(i+1),dfs(i+2))
11            return dp[i]
12
13        return min(dfs(0),dfs(1))