# Last updated: 5/7/2026, 1:25:40 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        if not nums:
4            return 0
5        if len(nums) == 1:
6            return nums[0]
7        dp=[0]*(len(nums))
8        dp[0],dp[1]=nums[0],max(nums[0],nums[1])
9        for i in range(2,len(nums)):
10            dp[i]=max(dp[i-1],nums[i]+dp[i-2])
11
12        return dp[-1]
13
14
15        