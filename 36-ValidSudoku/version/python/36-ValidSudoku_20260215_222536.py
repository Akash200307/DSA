# Last updated: 2/15/2026, 10:25:36 PM
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        
4        for i in range(9):
5            s=set()
6            for j in range(9):
7                piece=board[i][j]
8                if piece in s:
9                    return False
10                elif piece!=".":
11                    s.add(piece)
12        
13        for i in range(9):
14            s=set()
15            for j in range(9):
16                piece=board[j][i]
17                if piece in s:
18                    return False
19                elif piece!=".":
20                    s.add(piece)
21        
22        starts=[
23            (0,0),(0,3),(0,6),
24            (3,0),(3,3),(3,6),
25            (6,0),(6,3),(6,6)
26        ]
27
28        for i,j in starts:
29            s=set()
30            for r in range(i,i+3):
31                for c in range(j,j+3):
32                    piece=board[r][c]
33                    if piece in s:
34                        return False
35                    elif piece!=".":
36                        s.add(piece)
37        return True
38