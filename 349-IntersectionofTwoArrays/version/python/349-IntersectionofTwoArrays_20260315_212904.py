# Last updated: 3/15/2026, 9:29:04 PM
1class Solution:
2    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        s1=set(nums1)
4        s2=set(nums2)
5
6        return list(s1&s2)