# Last updated: 3/12/2026, 9:48:11 PM
1class DSU:
2    def __init__(self, n):
3        self.parent = list(range(n))
4        self.rank = [0] * n
5        self.components = n
6
7    def find(self, x):
8        if self.parent[x] != x:
9            self.parent[x] = self.find(self.parent[x])
10        return self.parent[x]
11
12    def unite(self, a, b):
13        pa = self.find(a)
14        pb = self.find(b)
15
16        if pa == pb:
17            return False
18
19        if self.rank[pa] < self.rank[pb]:
20            pa, pb = pb, pa
21
22        self.parent[pb] = pa
23
24        if self.rank[pa] == self.rank[pb]:
25            self.rank[pa] += 1
26
27        self.components -= 1
28        return True
29
30
31class Solution:
32    def canAchieve(self, n, edges, k, x):
33        dsu = DSU(n)
34
35        # Mandatory edges
36        for u, v, s, must in edges:
37            if must == 1:
38                if s < x:
39                    return False
40                if not dsu.unite(u, v):
41                    return False
42
43        # Free optional edges
44        for u, v, s, must in edges:
45            if must == 0 and s >= x:
46                dsu.unite(u, v)
47
48        # Upgrade edges
49        used_upgrades = 0
50
51        for u, v, s, must in edges:
52            if must == 0 and s < x and 2 * s >= x:
53                if dsu.unite(u, v):
54                    used_upgrades += 1
55                    if used_upgrades > k:
56                        return False
57
58        return dsu.components == 1
59
60    def maxStability(self, n, edges, k):
61        # Check mandatory edges cycle
62        dsu = DSU(n)
63        for u, v, s, must in edges:
64            if must == 1:
65                if not dsu.unite(u, v):
66                    return -1
67
68        low, high = 1, 200000
69        ans = -1
70
71        while low <= high:
72            mid = (low + high) // 2
73
74            if self.canAchieve(n, edges, k, mid):
75                ans = mid
76                low = mid + 1
77            else:
78                high = mid - 1
79
80        return ans