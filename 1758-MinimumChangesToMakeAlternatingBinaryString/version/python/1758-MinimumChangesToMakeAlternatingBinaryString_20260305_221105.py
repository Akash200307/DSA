# Last updated: 3/5/2026, 10:11:05 PM
1class Solution:
2    def minOperations(self, s: str) -> int:
3        a,b,n=0,0,len(s)
4
5        for ch in s:
6            if int(ch)==b:
7                a+=1
8            b^=1
9        
10        return min(n-a,a)