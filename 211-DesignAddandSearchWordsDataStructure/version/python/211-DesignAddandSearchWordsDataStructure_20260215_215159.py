# Last updated: 2/15/2026, 9:51:59 PM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        path=set()
4        ROWS=len(board)
5        COLS=len(board[0])
6        def dfs(row,col,i):
7            if i==len(word):
8                return True
9
10            if row<0 or col<0 or row>=ROWS or col>=COLS or word[i]!=board[row][col] or (row,col) in path:
11                return False
12            path.add((row,col))
13            if dfs(row-1,col,i+1) or dfs(row+1,col,i+1) or dfs(row,col+1,i+1) or dfs(row,col-1,i+1):
14                return True
15            path.remove((row,col))
16
17        for i in range(ROWS):
18            for j in range(COLS):
19              if  dfs(i,j,0):
20                return True
21        return False
22             