# Last updated: 2/9/2026, 11:15:51 PM
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        
4        for row in range(9):
5            s=set()
6            for col in range(9):
7                item=board[row][col]
8                if item in s:
9                    return False
10                elif item !=".":
11                    s.add(item)
12
13        
14        for row in range(9):
15            s=set()
16            for col in range(9):
17                item=board[col][row]
18                if item in s:
19                    return False
20                elif item !=".":
21                    s.add(item)
22
23        
24        starts=[(0,0),(0,3),(0,6),
25                (3,0),(3,3),(3,6),
26                (6,0),(6,3),(6,6)
27        ]
28
29
30        for i,j in starts:
31            s=set()
32            for r in range(i,i+3):
33                for c in range(j,j+3):
34                    item=board[r][c]
35
36                    if item in s:
37                        return False
38                    elif item!=".":
39                        s.add(item)
40        return True