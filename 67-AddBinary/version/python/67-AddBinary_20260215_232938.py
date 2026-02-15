# Last updated: 2/15/2026, 11:29:38 PM
1class Solution:
2    def addBinary(self, a, b) -> str:
3        x, y = int(a, 2), int(b, 2)
4        while y:
5            x, y = x ^ y, (x & y) << 1
6        return bin(x)[2:]
7