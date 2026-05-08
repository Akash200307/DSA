# Last updated: 5/8/2026, 9:00:48 PM
1class Solution:
2
3    def countSubstrings(self, s: str) -> int:
4        res = 0
5
6        for i in range(len(s)):
7            res += self.countPali(s, i, i)
8            res += self.countPali(s, i, i + 1)
9        return res
10
11    def countPali(self, s, l, r):
12        res = 0
13        while l >= 0 and r < len(s) and s[l] == s[r]:
14            res += 1
15            l -= 1
16            r += 1
17        return res