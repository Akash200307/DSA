# Last updated: 4/3/2026, 10:26:12 PM
1class Solution:
2    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
3        n = len(robots)
4
5        robots = sorted(zip(robots, distance))
6        walls.sort()
7
8        robots.append((10**18, 0))
9
10        def count_walls(l, r):
11            if l > r:
12                return 0
13            return bisect.bisect_right(walls, r) - bisect.bisect_left(walls, l)
14
15        dp = [[0, 0] for _ in range(n)]
16
17        pos, dist = robots[0]
18
19        left_gain = count_walls(pos - dist, pos)
20        right_gain = count_walls(pos, min(robots[1][0] - 1, pos + dist))
21
22        dp[0][0] = left_gain
23        dp[0][1] = right_gain
24
25        for i in range(1, n):
26            pos, dist = robots[i]
27            prev_pos, prev_dist = robots[i - 1]
28
29
30            left_l = max(pos - dist, prev_pos + 1)
31            left_r = pos
32            left_gain = count_walls(left_l, left_r)
33
34            right_l = pos
35            right_r = min(robots[i + 1][0] - 1, pos + dist)
36            right_gain = count_walls(right_l, right_r)
37
38            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1]) + right_gain
39
40            dp[i][0] = dp[i - 1][0] + left_gain
41
42            overlap_l = left_l
43            overlap_r = min(prev_pos + prev_dist, pos - 1)
44            overlap = count_walls(overlap_l, overlap_r)
45
46            dp[i][0] = max(dp[i][0], dp[i - 1][1] + left_gain - overlap)
47
48        return max(dp[n - 1][0], dp[n - 1][1])