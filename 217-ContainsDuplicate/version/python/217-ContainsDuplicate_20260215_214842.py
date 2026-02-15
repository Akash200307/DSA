# Last updated: 2/15/2026, 9:48:42 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        
4        s=set()
5
6        for i in nums:
7            if i in s:
8                return True
9            s.add(i)
10        return False