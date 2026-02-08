# Last updated: 2/8/2026, 11:01:44 PM
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        freq=collections.defaultdict(bool)
4
5        ans=[]
6        self.findPermute(nums,ans,[],freq)
7        return ans
8    def findPermute(self,arr,res,sol,freq):
9        if len(sol)==len(arr):
10            res.append(sol[:])
11            return
12        
13
14        for i in arr:
15            if not freq[i]:
16                freq[i]=True
17                sol.append(i)
18                self.findPermute(arr,res,sol,freq)
19                sol.pop()
20                freq[i]=False
21
22