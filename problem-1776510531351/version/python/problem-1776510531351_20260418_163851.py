# Last updated: 4/18/2026, 4:38:51 PM
1class Solution:
2    def mirrorDistance(self, n: int) -> int:
3        rev, x=0, n
4        while x>0:
5            x, r=divmod(x, 10)
6            rev=10*rev+r
7        return abs(rev-n)
8        
9        