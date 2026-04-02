# Last updated: 4/2/2026, 9:35:34 PM
1class Solution(object):
2    def maximumAmount(self, coins):
3        n = len(coins)
4        m = len(coins[0])
5        dp = [[[-10**9] * 3 for _ in range(m)] for _ in range(n)]
6
7        dp[0][0][1] = dp[0][0][2] = 0
8        dp[0][0][0] = coins[0][0]
9
10        for i in range(n):
11            for j in range(m):
12                for k in range(3):
13                    if i:
14                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k] + coins[i][j])
15                    if i and k:
16                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - 1])
17                    if j:
18                        dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k] + coins[i][j])
19                    if j and k:
20                        dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k - 1])
21
22        return max(dp[n - 1][m - 1])