# Last updated: 4/24/2026, 10:43:38 PM
1class Solution:
2    def furthestDistanceFromOrigin(self, moves: str) -> int:
3        left = moves.count('L')
4        right = moves.count('R')
5        blanks = moves.count('_')
6
7        return abs(left - right) + blanks