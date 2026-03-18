# Last updated: 3/18/2026, 9:06:37 PM
1# Added using AI
2class Solution:
3    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
4        m, n = len(grid), len(grid[0])
5        ans = 0
6        px = [[0] * (n + 1) for _ in range(m + 1)]
7        for i in range(m):
8            for j in range(n):
9                px[i+1][j+1] = grid[i][j] + px[i][j+1] + px[i+1][j] - px[i][j]
10                if px[i+1][j+1] <= k:
11                    ans += 1
12        return ans