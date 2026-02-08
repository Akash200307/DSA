# Last updated: 2/8/2026, 9:50:09 PM
1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        res=[]
4        self.findCombo(candidates,res,[],target,0,0)
5        return res
6    def findCombo(self,arr,res,sol,target,curr,i):
7        if i==len(arr):
8            if curr==target:
9                res.append(sol.copy())
10            return
11            
12        if i<len(arr) and curr<=target:
13            sol.append(arr[i])
14            self.findCombo(arr,res,sol,target,curr+arr[i],i)
15            sol.pop()
16        self.findCombo(arr,res,sol,target,curr,i+1)
17        
18            
19        
20        