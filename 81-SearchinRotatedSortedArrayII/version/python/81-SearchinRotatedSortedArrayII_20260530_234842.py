# Last updated: 5/30/2026, 11:48:42 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> bool:
3        low,high=0,len(nums)-1
4
5        while low<=high:
6            mid =low+(high-low)//2
7            if nums[mid]==target:
8                return True
9
10            if nums[low]==nums[mid]==nums[high]:
11                low+=1
12                high-=1
13                continue
14            
15            
16            if nums[low]<=nums[mid]:
17                if nums[low]<=target<nums[mid]:
18                    high=mid-1
19                else:
20                    low=mid+1
21            # if nums[mid]<=nums[high]:
22            else:
23                if nums[mid]<target<=nums[high]:
24                    low=mid+1
25                else:
26                    high=mid-1
27        return False
28