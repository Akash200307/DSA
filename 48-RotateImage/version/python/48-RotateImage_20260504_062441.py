# Last updated: 5/4/2026, 6:24:41 AM
1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        ROWS,COLS=len(matrix),len(matrix[0])
7
8        for i in range(ROWS):
9            for j in range(i):
10                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
11
12
13        for i in range(ROWS):
14            matrix[i].reverse()
15        