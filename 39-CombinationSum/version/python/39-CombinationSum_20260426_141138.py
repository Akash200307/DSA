# Last updated: 4/26/2026, 2:11:38 PM
1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        res=[]
4        candidates.sort()
5
6        def backtrack(start,path,cur):
7            if cur==target:
8                res.append(path[:])
9                return
10            if cur>target:
11                return
12            
13            for i in range(start,len(candidates)):
14                if cur+candidates[i]>target:
15                    return
16                path.append(candidates[i])
17                backtrack(i,path,cur+candidates[i])
18                path.pop()
19                
20        backtrack(0,[],0)
21        return res