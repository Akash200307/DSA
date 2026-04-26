# Last updated: 4/26/2026, 1:15:18 PM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        res=[]
4        def backtrack(start,sub):
5            res.append(sub[:])
6            for i in range(start,len(nums)):
7                sub.append(nums[i])
8                backtrack(i+1,sub)
9                sub.pop()
10        backtrack(0,[])
11        return res
12