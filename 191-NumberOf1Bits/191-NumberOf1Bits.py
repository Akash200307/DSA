# Last updated: 2/3/2026, 9:40:44 PM
class Solution:
    def hammingWeight(self, n: int) -> int:
      res=0
      while(n!=0):
        n=n&(n-1)
        res=res+1
      return res
        