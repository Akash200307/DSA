# Last updated: 3/16/2026, 9:14:49 PM
1class Solution:
2    def getBiggestThree(self, grid):
3        m, n = len(grid), len(grid[0])
4        s = set()
5
6        for i in range(m):
7            for j in range(n):
8                s.add(grid[i][j])
9
10                k = 1
11                while True:
12                    if i-k<0 or i+k>=m or j-k<0 or j+k>=n:
13                        break
14
15                    total = 0
16
17                    r, c = i-k, j
18                    for t in range(k):
19                        total += grid[r+t][c+t]
20
21                    r, c = i, j+k
22                    for t in range(k):
23                        total += grid[r+t][c-t]
24
25                    r, c = i+k, j
26                    for t in range(k):
27                        total += grid[r-t][c-t]
28
29                    r, c = i, j-k
30                    for t in range(k):
31                        total += grid[r-t][c+t]
32
33                    s.add(total)
34                    k += 1
35
36        return sorted(s, reverse=True)[:3]