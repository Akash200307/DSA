# Last updated: 2/3/2026, 9:41:42 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      res=0
      for num in nums:
        res=num^res
      return res
        