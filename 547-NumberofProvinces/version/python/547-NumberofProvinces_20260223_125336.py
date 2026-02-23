# Last updated: 2/23/2026, 12:53:36 PM
1class Solution:
2    def findCircleNum(self, isConnected: List[List[int]]) -> int:
3        
4        graph=defaultdict(list)
5
6        for i in range(len(isConnected)):
7            for j in range(i+1,len(isConnected)):
8                if isConnected[i][j]:
9                    graph[i].append(j)
10                    graph[j].append(i)
11        res=0
12        q=deque()
13        vis=[False]*len(isConnected)
14        for i in range(len(isConnected)):
15            if not vis[i]:
16                q.append(i)
17                vis[i]=True
18                res+=1
19                while q:
20                    node=q.popleft()
21                    for nbr in graph[node]:
22                        if not vis[nbr]:
23                            vis[nbr]=True
24                            q.append(nbr)
25
26        return res
27
28            