# Last updated: 6/7/2026, 8:14:07 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        map={}
4
5        for k,v in enumerate(nums):
6            diff=target-v
7            if diff in map:
8                return [map[diff],k]
9            map[v]=k
10        return []
11