# Last updated: 6/3/2026, 9:13:50 PM
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        if len(haystack)<len(needle):
4            return -1
5        for i in range(len(haystack)):
6            if haystack[i:i+len(needle)]==needle:
7                return i
8        return -1
9        