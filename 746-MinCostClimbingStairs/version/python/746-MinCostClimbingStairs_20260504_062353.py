# Last updated: 5/4/2026, 6:23:53 AM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        dp=[0]*(len(cost)+1)
4        
5
6        for i in range(2,len(cost)+1):
7            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
8        
9        return dp[len(cost)]
10        
11        