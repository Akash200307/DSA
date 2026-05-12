# Last updated: 5/12/2026, 9:42:20 PM
1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3        dp=[[-1] * n for _ in range(m) ]
4        def dfs(i,j):
5            if i ==(m-1) and j==(n-1):
6                return 1
7            if i>=m or j>=n:
8                return 0
9            if dp[i][j]!=-1:
10                return dp[i][j]
11            
12            dp[i][j]=dfs(i,j+1) + dfs(i+1,j)
13            return dp[i][j]
14        
15        return dfs(0,0)