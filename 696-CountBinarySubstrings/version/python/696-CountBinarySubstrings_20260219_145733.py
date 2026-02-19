# Last updated: 2/19/2026, 2:57:33 PM
1class Solution:
2    def countBinarySubstrings(self, s: str) -> int:
3        
4        res=0
5        prev=0
6        curr=1
7        for i in range(1,len(s)):
8
9            if s[i-1]==s[i]:
10                curr+=1
11            else:
12                res+=min(curr,prev)
13                prev=curr
14                curr=1
15           
16        res+=min(curr,prev)
17
18        return res
19        
20
21