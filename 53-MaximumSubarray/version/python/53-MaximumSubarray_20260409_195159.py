# Last updated: 4/9/2026, 7:51:59 PM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        curr=nums[0]
4        max_s=nums[0]
5
6        for num in nums[1:]:
7
8            curr=max(num,curr+num)
9            max_s=max(max_s,curr)
10        return max_s