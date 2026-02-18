# Last updated: 2/18/2026, 10:42:10 PM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        
4
5        graph=defaultdict(list)
6
7        courses=prerequisites
8
9        for a,b in courses:
10            graph[a].append(b)
11
12        states=[0]*numCourses
13
14        def dfs(node):
15            state=states[node]
16
17            if state==2:
18                return True
19            if state==1:
20                return False
21            
22            states[node]=1
23
24            for nei in graph[node]:
25                if not dfs(nei):
26                    return False
27            
28            states[node]=2
29            return True
30
31
32        for i in range(numCourses):
33            if states[i]==0:
34                if not dfs(i):
35                    return False
36        return True