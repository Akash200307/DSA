# Last updated: 3/23/2026, 1:17:57 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        n=len(numbers)
4        l,r=0,n-1
5
6        while l<r:
7            curr=numbers[l]+numbers[r]
8            if curr==target:
9                return [l+1,r+1]
10            elif curr<target:
11                l+=1
12            else:
13                r-=1
14        
15