# Last updated: 3/22/2026, 9:42:37 PM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        freq=Counter(t)
4        count=len(t)
5        min_len=float('inf')
6        l=0
7        for r in range(len(s)):
8            char=s[r]
9            if char in freq:
10                if freq[char]>0:
11                    count-=1
12                freq[char]-=1
13            
14            while count==0:
15
16                if r-l+1 <min_len:
17                    min_len=r-l+1
18                    temp=l
19                if s[l] in freq:
20                    freq[s[l]]+=1
21                    if freq[s[l]]>0:
22                        count+=1
23                l+=1
24        
25        return "" if min_len==float("inf") else s[temp:temp+min_len]
26
27
28                
29