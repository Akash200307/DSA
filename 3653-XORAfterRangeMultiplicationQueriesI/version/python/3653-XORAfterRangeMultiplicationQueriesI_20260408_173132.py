# Last updated: 4/8/2026, 5:31:32 PM
1class Solution:
2    def xorAfterQueries(self, nums, queries):
3        mod = 1000000007
4
5        # Process each query
6        for t in queries:
7            l = t[0]
8            r = t[1]
9            k = t[2]
10            v = t[3]
11
12            idx = l
13
14            # Apply operation at step k
15            while idx <= r:
16                temp = nums[idx]
17                nums[idx] = (temp * v) % mod
18                idx += k
19
20        # Compute XOR of final array
21        ans = 0
22        for num in nums:
23            ans ^= num
24
25        return ans