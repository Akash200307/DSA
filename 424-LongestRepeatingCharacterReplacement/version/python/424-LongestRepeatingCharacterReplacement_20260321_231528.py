# Last updated: 3/21/2026, 11:15:28 PM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        
4        l=0
5        lon=0
6        counts=[0]*26
7
8        for r in range(len(s)):
9            counts[ord(s[r])-ord('A')]+=1
10            while (r-l+1)-max(counts)>k:
11                counts[ord(s[l])-ord('A')]-=1
12                l+=1
13            lon=max(lon,r-l+1)
14        return lon
15