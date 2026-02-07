# Last updated: 2/7/2026, 11:50:34 PM
1class Solution:
2    def solveNQueens(self, n: int) -> List[List[str]]:
3        res = []
4        board = [["."] * n for i in range(n)]
5
6        def backtrack(r):
7            if r == n:
8                copy = ["".join(row) for row in board]
9                res.append(copy)
10                return
11            for c in range(n):
12                if self.isSafe(r, c, board):
13                    board[r][c] = "Q"
14                    backtrack(r + 1)
15                    board[r][c] = "."
16
17        backtrack(0)
18        return res
19
20    def isSafe(self, r: int, c: int, board):
21        row = r - 1
22        while row >= 0:
23            if board[row][c] == "Q":
24                return False
25            row -= 1
26
27        row, col = r - 1, c - 1
28        while row >= 0 and col >= 0:
29            if board[row][col] == "Q":
30                return False
31            row -= 1
32            col -= 1
33
34        row, col = r - 1, c + 1
35        while row >= 0 and col < len(board):
36            if board[row][col] == "Q":
37                return False
38            row -= 1
39            col += 1
40        return True