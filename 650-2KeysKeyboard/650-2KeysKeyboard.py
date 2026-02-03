# Last updated: 2/3/2026, 9:38:44 PM
class Solution:
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0
        step=0
        factor=2
        while n>1:
            while n%factor==0:
                step=step+factor
                n//=factor
            factor+=1
        return step

        
    