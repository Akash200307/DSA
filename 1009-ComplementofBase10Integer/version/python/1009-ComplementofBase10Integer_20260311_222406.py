# Last updated: 3/11/2026, 10:24:06 PM
1class Solution:
2    def bitwiseComplement(self, n: int) -> int:
3        if n == 0: return 1
4        mask = n
5        for i in (1, 2, 4, 8, 16):
6            mask |= mask >> i
7        return ~n & mask