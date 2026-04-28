# Last updated: 4/28/2026, 3:16:56 PM
1class Solution:
2    def fib(self, n: int) -> int:
3        dp=[-1]*(n+1)
4        
5        def helper(n):
6            if n<=1:
7                return n
8            
9            if dp[n]!=-1:
10                return dp[n]
11            dp[n] = helper(n-1)+helper(n-2)
12            return dp[n]
13        return helper(n)