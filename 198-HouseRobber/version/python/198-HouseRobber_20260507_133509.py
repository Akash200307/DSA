# Last updated: 5/7/2026, 1:35:09 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        rob1,rob2=0,0
4
5        for num in nums:
6            temp=max(rob1,num+rob2)
7            rob2=rob1
8            rob1=temp
9        
10        return rob1
11
12
13        