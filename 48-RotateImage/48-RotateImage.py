# Last updated: 2/3/2026, 9:43:13 PM
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS,COLS=len(matrix),len(matrix[0])

        for i in range(ROWS):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]


        for i in range(ROWS):
            matrix[i].reverse()
        