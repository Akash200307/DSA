# Last updated: 5/3/2026, 8:25:14 PM
1class Solution:
2    def rotateString(self, s: str, goal: str) -> bool:
3        if len(s)!=len(goal):
4            return False
5
6        double_s=s+s
7        return goal in double_s
8        