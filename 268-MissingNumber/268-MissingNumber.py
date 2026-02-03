# Last updated: 2/3/2026, 9:39:37 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      n=len(nums)
      x=n
      for i in range(n):
        x=x^i^nums[i]
      return x
        