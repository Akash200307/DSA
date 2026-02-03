# Last updated: 2/3/2026, 9:38:52 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        k=len(s1)
        l=0
        for r in range(len(s2)+1):
            temp=s2[l:r]
            if Counter(s1)==Counter(temp):
                return True
            if r-l+1>k:
                l+=1
        return False



        