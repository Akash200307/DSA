# Last updated: 5/7/2026, 1:38:30 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        rob1,rob2=0,0
4
5        for num in nums:
6            rob1,rob2=max(rob1,num+rob2),rob1
7        
8        return rob1
9
10
11        