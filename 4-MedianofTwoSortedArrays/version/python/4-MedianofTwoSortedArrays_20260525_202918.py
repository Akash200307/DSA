# Last updated: 5/25/2026, 8:29:18 PM
1class Solution:
2    def findMedianSortedArrays(self, nums1, nums2):
3        # Merge the arrays into a single sorted array.
4        merged = nums1 + nums2
5
6        # Sort the merged array.
7        merged.sort()
8
9        # Calculate the total number of elements in the merged array.
10        total = len(merged)
11
12        if total % 2 == 1:
13            # If the total number of elements is odd, return the middle element as the median.
14            return float(merged[total // 2])
15        else:
16            # If the total number of elements is even, calculate the average of the two middle elements as the median.
17            middle1 = merged[total // 2 - 1]
18            middle2 = merged[total // 2]
19            return (float(middle1) + float(middle2)) / 2.0