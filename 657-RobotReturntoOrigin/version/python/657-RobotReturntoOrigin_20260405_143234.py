# Last updated: 4/5/2026, 2:32:34 PM
1class Solution:
2    def judgeCircle(self, moves: str) -> bool:
3        return moves.count('L') == moves.count('R') and \
4               moves.count('U') == moves.count('D')