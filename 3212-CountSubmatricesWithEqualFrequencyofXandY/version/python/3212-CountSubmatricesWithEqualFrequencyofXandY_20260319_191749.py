# Last updated: 3/19/2026, 7:17:49 PM
1class Solution:
2    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
3        m, n = len(grid), len(grid[0])
4        px = [[0] * (n + 1) for _ in range(m + 1)]  # prefix count of 'X'
5        py = [[0] * (n + 1) for _ in range(m + 1)]  # prefix count of 'Y'
6        ans = 0
7
8        for i in range(1, m + 1):
9            for j in range(1, n + 1):
10                px[i][j]=px[i-1][j]+px[i][j-1]+(grid[i-1][j-1]=='X')-px[i-1][j-1]
11                py[i][j]=py[i-1][j]+py[i][j-1]+(grid[i-1][j-1]=='Y')-py[i-1][j-1]
12
13                if px[i][j]>0 and px[i][j]==py[i][j]:
14                    ans+=1
15
16
17        return ans