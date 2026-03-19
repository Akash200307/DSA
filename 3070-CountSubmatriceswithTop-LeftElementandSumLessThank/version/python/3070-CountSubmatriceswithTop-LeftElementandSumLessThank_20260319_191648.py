# Last updated: 3/19/2026, 7:16:48 PM
1# Added using AI
2class Solution:
3    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
4        m, n = len(grid), len(grid[0])
5        px=[[0]*(n+1) for _ in range(m+1)]
6        res=0
7        for i in range(1,m+1):
8            for j in range(1,n+1):
9                px[i][j]=grid[i-1][j-1]+px[i-1][j]+px[i][j-1]-px[i-1][j-1]
10                if px[i][j]<=k:
11                    res+=1
12        return res