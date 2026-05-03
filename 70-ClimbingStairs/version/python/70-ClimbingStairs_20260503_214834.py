# Last updated: 5/3/2026, 9:48:34 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n<=2:
4            return n
5        
6        dp=[0]*(n+1)
7        dp[1]=1
8        dp[2]=2
9        for i in range(3,n+1):
10            dp[i]=dp[i-1]+dp[i-2]
11        return dp[n]