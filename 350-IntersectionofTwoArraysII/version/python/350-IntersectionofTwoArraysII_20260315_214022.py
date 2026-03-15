# Last updated: 3/15/2026, 9:40:22 PM
1class Solution:
2    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        nums1.sort()
4        nums2.sort()
5
6        
7        ans,i,j=[],0,0
8
9        while i<len(nums1) and j<len(nums2):
10
11            if nums1[i]<nums2[j]:
12                i+=1
13            elif nums1[i]>nums2[j]:
14                j+=1
15            else:
16                ans.append(nums1[i])
17                i+=1
18                j+=1
19        return ans