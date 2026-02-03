# Last updated: 2/3/2026, 9:42:59 PM
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_set=set()
        ROWS,COLS=len(matrix),len(matrix[0])
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j]==0:
                    zero_set.add((i,j))

        for r,c in zero_set:
            for i in range(COLS):
                matrix[r][i]=0
            for j in range(ROWS):
                matrix[j][c]=0
                
