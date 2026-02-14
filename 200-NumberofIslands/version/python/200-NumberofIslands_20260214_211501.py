# Last updated: 2/14/2026, 9:15:01 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        
4        rows=len(grid)
5        cols=len(grid[0])
6
7        if not grid:
8            return 0
9
10        def dfs(r,c):
11
12            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]=="0":
13                return
14            
15            grid[r][c]="0"
16
17            dfs(r+1,c)
18            dfs(r-1,c)
19            dfs(r,c+1)
20            dfs(r,c-1)
21
22        islands=0
23        for i in range(rows):
24            for j in range(cols):
25                if grid[i][j]=="1":
26                    dfs(i,j)
27                    islands+=1
28        return islands