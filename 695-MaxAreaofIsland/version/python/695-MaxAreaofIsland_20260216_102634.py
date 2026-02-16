# Last updated: 2/16/2026, 10:26:34 AM
1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        rows=len(grid)
4        cols=len(grid[0])
5        maxArea=0
6        if not grid:
7            return 0
8
9        def dfs(r,c):
10
11            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0:
12                return 0
13            
14            grid[r][c]=0
15            area=1
16            area +=dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
17            return area
18
19        
20
21        for i in range(rows):
22            for j in range(cols):
23                if grid[i][j]==1:
24                    area=dfs(i,j)
25                    maxArea=max(area,maxArea)
26        return maxArea