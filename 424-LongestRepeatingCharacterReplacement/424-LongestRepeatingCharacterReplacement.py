# Last updated: 2/3/2026, 9:39:23 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        l=0
        max_freq=0
        res=0
        for r in range(len(s)):
            freq[s[r]]=1 + freq.get(s[r],0)
            max_freq=max(max_freq,freq[s[r]])
            if (r-l)+1 - max_freq>k:
                freq[s[l]]-=1
                l+=1
            
        return len(s)- l
        

        