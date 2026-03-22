# Last updated: 3/22/2026, 8:23:04 PM
1class Solution:
2    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
3        for x in range(4):
4            if mat == target: return True
5            mat = [list(r) for r in zip(*mat[::-1])]
6        return False