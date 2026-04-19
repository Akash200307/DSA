# Last updated: 4/20/2026, 12:07:31 AM
1class Solution:
2    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
3        max_dist = 0
4        m, n = len(nums1), len(nums2)
5
6        for i in range(m):
7            lo, hi = i, n - 1
8
9            while lo <= hi:
10                mid = (lo + hi) // 2
11
12                if nums2[mid] >= nums1[i]:
13                    max_dist = max(max_dist, mid - i)
14                    lo = mid + 1
15                else:
16                    hi = mid - 1
17
18        return max_dist