# Last updated: 2/6/2026, 9:29:30 PM
1class Solution:
2
3    def findPermute(self,sol,arr,res,freq):
4        if len(sol)==len(arr):
5            res.append(sol.copy())
6            return
7
8        for i in arr:
9            if not freq[i]:
10                freq[i]=True
11                sol.append(i)
12                self.findPermute(sol,arr,res,freq)
13                sol.pop()
14                freq[i]=False
15
16    def permute(self, nums: List[int]) -> List[List[int]]:
17        ans=[]
18        freq=collections.defaultdict(int)
19        self.findPermute([],nums,ans,freq)
20        return ans