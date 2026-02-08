# Last updated: 2/8/2026, 9:10:26 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        
4        map={}
5
6        for k,v in enumerate(nums):
7            diff=target-v
8
9            if diff in map:
10                return [map[diff],k]
11
12            map[v]=k
13        
14        return []
15                
16
17            
18
19