# Last updated: 6/17/2026, 12:10:57 AM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        nums=set(nums)
4        mx=0
5
6        for num in nums:
7            if num-1 not in nums:
8                count=0
9                curr=num
10                while curr in nums:
11                    count+=1
12                    curr+=1
13                mx=max(mx,count)
14        return mx