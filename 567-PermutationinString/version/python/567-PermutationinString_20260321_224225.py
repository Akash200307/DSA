# Last updated: 3/21/2026, 10:42:25 PM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        s1_counts=[0]*26
4        s2_counts=[0]*26
5
6        if len(s1)>len(s2):
7            return False
8        for i in range(len(s1)):
9            s1_counts[ord(s1[i])-ord('a')]+=1
10            s2_counts[ord(s2[i])-ord('a')]+=1
11        
12        if s1_counts==s2_counts:
13            return True
14        
15        for i in range(len(s1),len(s2)):
16            s2_counts[ord(s2[i])-ord('a')]+=1
17            s2_counts[ord(s2[i-len(s1)])-ord('a')]-=1
18            if s1_counts==s2_counts:
19                return True
20        
21        return False
22