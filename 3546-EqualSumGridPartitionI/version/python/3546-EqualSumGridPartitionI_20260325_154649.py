# Last updated: 3/25/2026, 3:46:49 PM
1class Solution:
2    def canPartitionGrid(self, grid):
3        m, n = len(grid), len(grid[0])
4
5        rowSum = [0] * m
6        colSum = [0] * n
7        total = 0
8
9        # Compute sums
10        for i in range(m):
11            for j in range(n):
12                rowSum[i] += grid[i][j]
13                colSum[j] += grid[i][j]
14                total += grid[i][j]
15
16        if total % 2:
17            return False
18
19        if self.check(rowSum, total):
20            return True
21
22        if self.check(colSum, total):
23            return True
24
25        return False
26
27    def check(self, arr, total):
28        left = arr[0]
29        right = total - left
30
31        for i in range(1, len(arr)):
32            if left == right:
33                return True
34            elif left > right:
35                return False
36            left += arr[i]
37            right -= arr[i]
38
39        return False