# Last updated: 2/17/2026, 10:42:16 AM
1class Solution:
2    def orangesRotting(self, grid: List[List[int]]) -> int:
3        Rows=len(grid)
4        Cols=len(grid[0])
5        fresh,time=0,0
6        q=collections.deque()
7        for i in range(Rows):
8            for j in range(Cols):
9                if grid[i][j]==1:
10                    fresh+=1
11                if grid[i][j]==2:
12                    q.append((i,j))
13        
14        directions =[(1,0),(-1,0),(0,1),(0,-1)]
15        while q and fresh>0:
16            for i in range(len(q)):
17                r,c=q.popleft()
18                for dr,dc in directions:
19                    row,col=dr+r,dc+c
20                    if ( row in range(Rows) and col in range(Cols) and grid[row][col]==1):
21                        grid[row][col]=2
22                        q.append((row,col))
23                        fresh-=1
24            time+=1
25        return time if fresh==0 else -1
26            
27
28
29