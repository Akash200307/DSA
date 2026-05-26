# Last updated: 5/26/2026, 10:26:43 PM
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3
4        strs.sort()
5        first=strs[0]
6        last=strs[-1]
7        mini=min(len(first),len(last))
8        res=""
9        for i in range(mini):
10            if first[i]!=last[i]:
11                return res
12            res+=first[i]
13        return res
14
15        