# Last updated: 2/3/2026, 9:37:16 PM
class Solution:
    def maxDepth(self, s: str) -> int:
        cnt=0
        res=0

        for ch in s:
            if ch=="(":
                cnt+=1
            if ch==")":
                cnt-=1
            res=max(res,cnt)
        return res


    
