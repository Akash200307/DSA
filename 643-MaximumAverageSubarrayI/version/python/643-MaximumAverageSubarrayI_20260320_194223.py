# Last updated: 3/20/2026, 7:42:23 PM
1class Solution:
2    def findMaxAverage(self, nums: List[int], k: int) -> float:
3        
4        n=len(nums)
5        curr_sum=0
6
7        for i in range(k):
8            curr_sum+=nums[i]
9        
10        max_avg=curr_sum/k
11
12        for i in range(k,n):
13            curr_sum+=nums[i]
14            curr_sum-=nums[i-k]
15            avg=curr_sum/k
16            max_avg=max(avg,max_avg)
17        return max_avg
18