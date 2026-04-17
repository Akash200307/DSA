# Last updated: 4/17/2026, 8:24:07 PM
1class Solution(object):
2    def reverse(self, x):
3        rev = 0
4        while x > 0:
5            rev = rev * 10 + x % 10
6            x //= 10
7        return rev
8
9    def minMirrorPairDistance(self, nums):
10        mpp = {}
11        n = len(nums)
12        ans = 10 ** 6
13
14        for i in range(n):
15            if nums[i] in mpp:
16                ans = min(ans, i - mpp[nums[i]])
17            mpp[self.reverse(nums[i])] = i
18
19        return -1 if ans == 10 ** 6 else ans