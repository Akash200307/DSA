# Last updated: 2/11/2026, 7:30:36 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        s=set()
4
5        for i in nums:
6            if i in s:
7                return True
8            s.add(i)
9        return False