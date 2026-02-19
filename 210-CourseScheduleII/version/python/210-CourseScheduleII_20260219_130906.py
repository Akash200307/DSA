# Last updated: 2/19/2026, 1:09:06 PM
1class Solution:
2
3    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
4
5        order = []
6
7        g = defaultdict(list)
8
9        for a, b in prerequisites:
10
11            g[a].append(b)
12
13        
14
15        UNVISITED, VISITING, VISITED = 0, 1, 2
16
17        states = [UNVISITED] * numCourses
18
19        
20
21        def dfs(i):
22
23            if states[i] == VISITING:
24
25                return False
26
27            elif states[i] == VISITED:
28
29                return True
30
31            states[i] = VISITING
32
33    
34
35            for nei in g[i]:
36
37                if not dfs(nei):
38
39                    return False
40
41    
42
43            states[i] = VISITED
44
45            order.append(i)
46
47            return True
48
49    
50
51        
52
53        for i in range(numCourses):
54
55            if not dfs(i):
56
57                return []
58
59        
60
61        return order # Time: O(V + E), Space: O(V + E)
62
63            
64
65    