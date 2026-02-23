# Last updated: 2/23/2026, 12:15:01 PM
1class Solution:
2    def hasAllCodes(self, s: str, k: int) -> bool:
3        
4        if len(s) < k:
5            return False
6
7        sub_s=set()
8        n=len(s)
9        for i in range(n-k+1):
10            num=s[i:i+k]
11            sub_s.add(num)
12        return len(sub_s)==1<<k