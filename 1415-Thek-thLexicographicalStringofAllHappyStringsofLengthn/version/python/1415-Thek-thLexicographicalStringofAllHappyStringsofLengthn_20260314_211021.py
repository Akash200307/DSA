# Last updated: 3/14/2026, 9:10:21 PM
1class Solution:
2    def getHappyString(self, n: int, k: int) -> str:
3        res=[]
4        sol=[]
5
6        def dfs():
7            if len(sol)==n:
8                res.append("".join(sol))
9                return
10            if len(res) >=k:
11                return
12            
13            for c in 'abc':
14                if not sol or sol[-1]!=c:
15                    sol.append(c)
16                    dfs()
17                    sol.pop()
18        dfs()
19
20        return res[k-1] if len(res)>=k else ""
21            
22            