# Last updated: 3/22/2026, 10:32:57 PM
1class Solution:
2    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
3        for i in range(4):
4            if mat==target: 
5                return True
6            else:
7                mat=[list(j) for j in zip(*mat[::-1])]
8        return False