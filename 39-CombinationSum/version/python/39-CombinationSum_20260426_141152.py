# Last updated: 4/26/2026, 2:11:52 PM
1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        res=[]
4        candidates.sort()
5
6        def backtrack(start,path,cur):
7            if cur==target:
8                res.append(path[:])
9                return
10           
11            
12            for i in range(start,len(candidates)):
13                if cur+candidates[i]>target:
14                    return
15                path.append(candidates[i])
16                backtrack(i,path,cur+candidates[i])
17                path.pop()
18                
19        backtrack(0,[],0)
20        return res