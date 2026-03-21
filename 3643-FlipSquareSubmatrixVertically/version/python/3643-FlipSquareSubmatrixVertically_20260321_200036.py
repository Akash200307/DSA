# Last updated: 3/21/2026, 8:00:36 PM
1class Solution:
2    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
3        for i in range(k >> 1):
4            row1 = grid[x + i]
5            row2 = grid[x + k - 1 - i]
6            for j in range(k):
7                row1[y + j], row2[y + j] = row2[y + j], row1[y + j]
8        
9        return grid