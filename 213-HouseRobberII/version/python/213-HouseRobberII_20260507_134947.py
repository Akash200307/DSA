# Last updated: 5/7/2026, 1:49:47 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3
4        
5        if len(nums)==1:
6            return nums[0]
7        def helper(houses):
8            rob1,rob2=0,0
9            for h in houses:
10                rob1,rob2=max(rob1,h+rob2),rob1
11            return rob1
12        return max(helper(nums[:-1]),helper(nums[1:]))
13