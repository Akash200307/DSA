# Last updated: 4/26/2026, 3:59:22 PM
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        res=[]
4        def backtrack(path,visit):
5            if len(path)==len(nums):
6                res.append(path[:])
7                return
8            
9            for i in range(len(nums)):
10                if not visit[i]:
11                    visit[i]=True
12                    path.append(nums[i])
13                    backtrack(path,visit)
14                    path.pop()
15                    visit[i]=False
16        backtrack([],[False]*len(nums))
17        return res
18
19