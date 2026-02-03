# Last updated: 2/3/2026, 9:38:24 PM
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False

        double_s=s+s
        return goal in double_s
        