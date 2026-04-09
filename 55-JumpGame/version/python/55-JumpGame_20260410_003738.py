# Last updated: 4/10/2026, 12:37:38 AM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3
4        if len(nums)<=1:
5            return True
6        size=len(nums)
7        max_reach=0
8        for i in range(len(nums)):
9            if i >max_reach:
10                return False
11            max_reach=max(max_reach,nums[i]+i)
12
13            if max_reach>=size-1:
14                return True
15    