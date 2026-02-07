# Last updated: 2/8/2026, 12:05:12 AM
1class Solution:
2    def solveNQueens(self, n: int) -> List[List[str]]:
3        res = []
4        board = [["."] * n for i in range(n)]
5
6        def backtrack(r):
7            if r==n:
8                res.append(["".join(row) for row in board])
9                return
10            
11            for c in range(n):
12                if self.isSafe(r,c,board):
13                    board[r][c]="Q"
14                    backtrack(r+1)
15                    board[r][c]="."
16        backtrack(0)
17        return res
18
19    def isSafe(self, r: int, c: int, board):
20        row = r - 1
21        while row >= 0:
22            if board[row][c] == "Q":
23                return False
24            row -= 1
25
26        row, col = r - 1, c - 1
27        while row >= 0 and col >= 0:
28            if board[row][col] == "Q":
29                return False
30            row -= 1
31            col -= 1
32
33        row=r-1
34        col=c+1
35
36        while row>=0 and col<len(board):
37            if board[row][col]=="Q":
38                return False
39            row-=1
40            col+=1
41        return True