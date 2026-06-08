# Last updated: 6/8/2026, 11:00:57 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        
4        char_set=set()
5        res=0
6        l=0
7
8        for r in range(len(s)):
9            
10            while s[r] in char_set:
11                char_set.remove(s[l])
12                l+=1
13            char_set.add(s[r])
14
15            res=max(res,len(char_set))
16        
17        return res
18            
19