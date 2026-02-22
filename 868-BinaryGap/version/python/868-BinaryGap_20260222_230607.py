# Last updated: 2/22/2026, 11:06:07 PM
1class Solution:
2    def binaryGap(self, n: int) -> int:
3        bins=format(n,'b')
4
5        prev=-1
6
7        gap=0
8
9        for i in range(len(bins)):
10            if bins[i]=='1':
11                if prev!=-1:
12                    gap=max(gap,i-prev)
13                prev=i
14        return gap
15
16        
17
18
19       