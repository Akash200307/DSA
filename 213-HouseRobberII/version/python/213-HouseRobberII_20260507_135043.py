# Last updated: 5/7/2026, 1:50:43 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        # circle of houses
        # cannot rob 2 adjacent houses

        def robber(arr):
            prev2 = prev1= 0
            for point in arr:
                curr = max(prev2 + point, prev1)
                prev2 = prev1
                prev1 = curr
            return curr

        return max(robber(nums[:-1]), robber(nums[1:]))