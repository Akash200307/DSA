# Last updated: 2/17/2026, 11:15:02 PM
1class Solution:
2    def solve(self, board: List[List[str]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        """
6        Rows=len(board)
7        Cols=len(board[0])
8
9        
10        def dfs(r,c):
11
12            if r<0 or c<0 or r>=Rows or c>=Cols or board[r][c]!="O":
13                return 
14            board[r][c]="T"
15            dfs(r+1,c)
16            dfs(r-1,c)
17            dfs(r,c+1)
18            dfs(r,c-1)
19        
20        for i in range(Rows):
21            for j in range(Cols):
22                if board[i][j]=="O" and (i in [0,Rows-1] or j in [0,Cols-1]):
23                    dfs(i,j)
24        
25        for i in range(Rows):
26            for j in range(Cols):
27                if board[i][j]=="O":
28                    board[i][j]="X"
29        
30        for i in range(Rows):
31            for j in range(Cols):
32                if board[i][j]=="T":
33                    board[i][j]="O"
34
35