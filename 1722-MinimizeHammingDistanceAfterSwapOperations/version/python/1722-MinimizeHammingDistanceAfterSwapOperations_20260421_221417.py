# Last updated: 4/21/2026, 10:14:17 PM
1class Solution:
2    def minimumHammingDistance(self, source: list[int], target: list[int], allowedSwaps: list[list[int]]) -> int:
3        n = len(source)
4        parent = list(range(n))
5
6        def find(x):
7            if parent[x] != x:
8                parent[x] = find(parent[x])
9            return parent[x]
10
11        def unite(a, b):
12            parent[find(a)] = find(b)
13
14        for a, b in allowedSwaps:
15            unite(a, b)
16
17        # Group source values by their component root
18        from collections import defaultdict, Counter
19        groups = defaultdict(list)
20        for i in range(n):
21            groups[find(i)].append(source[i])
22        groups = {root: Counter(vals) for root, vals in groups.items()}
23
24        hamming_dist = 0
25        for i in range(n):
26            root = find(i)
27            freq = groups[root]
28            if freq[target[i]] > 0:
29                freq[target[i]] -= 1  # matched, consume this source value
30            else:
31                hamming_dist += 1     # no match found in this component
32
33        return hamming_dist