# Last updated: 4/7/2026, 6:31:54 PM
1class Solution:
2    def findContentChildren(self, g: List[int], s: List[int]) -> int:
3
4        if not s or not g:
5            return 0
6        n=len(g)
7        m=len(s)
8        g.sort()
9        s.sort()
10        l=0
11        r=0
12        
13
14        while(l<n and r<m):
15            if (g[l]<=s[r]):
16                l+=1
17            r+=1
18        
19        return l