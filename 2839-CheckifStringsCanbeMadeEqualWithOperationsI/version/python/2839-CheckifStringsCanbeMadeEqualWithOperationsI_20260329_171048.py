# Last updated: 3/29/2026, 5:10:48 PM
1class Solution:
2    def canBeEqual(self, s1: str, s2: str) -> bool:
3        even1, odd1 = "", ""
4        even2, odd2 = "", ""
5        
6        for i in range(len(s1)):
7            if i % 2 == 0:
8                even1 += s1[i]
9                even2 += s2[i]
10            else:
11                odd1 += s1[i]
12                odd2 += s2[i]
13        
14        even1 = sorted(even1)
15        even2 = sorted(even2)
16        odd1 = sorted(odd1)
17        odd2 = sorted(odd2)
18        
19        return even1 == even2 and odd1 == odd2