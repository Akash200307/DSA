# Last updated: 2/3/2026, 9:42:58 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        top,bot=0,n*m-1
        while top<=bot:
            mid=(top+bot)//2
            row=mid//m
            col=mid%m
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                top=mid+1
            else:
                bot=mid-1
        return False
