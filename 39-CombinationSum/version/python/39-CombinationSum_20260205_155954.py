# Last updated: 2/5/2026, 3:59:54 PM
1class Solution:
2
3    def findCombo(self,i,arr,target,ans,sol):
4        if i==len(arr):
5            if target==0:
6                ans.append(sol.copy())
7            return
8        
9        if arr[i]<=target:
10            sol.append(arr[i])
11            self.findCombo(i,arr,target-arr[i],ans,sol)
12            sol.pop()
13        self.findCombo(i+1,arr,target,ans,sol)
14
15    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
16        ans=[]
17        self.findCombo(0,candidates,target,ans,[])
18        return ans