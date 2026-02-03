# Last updated: 2/3/2026, 9:40:07 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n>0 and n&(n-1)==0:
            return True
        else:
            return False
            