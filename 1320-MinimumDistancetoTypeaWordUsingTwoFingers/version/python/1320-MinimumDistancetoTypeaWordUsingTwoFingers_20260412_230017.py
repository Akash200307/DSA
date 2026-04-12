# Last updated: 4/12/2026, 11:00:17 PM
1class Solution:
2    def minimumDistance(self, word: str) -> int:
3        n = len(word)
4        BIG = 2**30
5        dp = [[0] * 26] + [[BIG] * 26 for _ in range(n - 1)]
6
7        def getDistance(p, q):
8            x1, y1 = p // 6, p % 6
9            x2, y2 = q // 6, q % 6
10            return abs(x1 - x2) + abs(y1 - y2)
11
12        for i in range(1, n):
13            cur, prev = ord(word[i]) - 65, ord(word[i - 1]) - 65
14            d = getDistance(prev, cur)
15            for j in range(26):
16                dp[i][j] = min(dp[i][j], dp[i - 1][j] + d)
17                if prev == j:
18                    for k in range(26):
19                        d0 = getDistance(k, cur)
20                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + d0)
21
22        ans = min(dp[n - 1])
23        return ans