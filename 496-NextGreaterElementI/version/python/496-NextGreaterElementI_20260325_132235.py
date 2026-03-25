# Last updated: 3/25/2026, 1:22:35 PM
1class Solution:
2    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        stk=[]
4        dic=defaultdict(int)
5        res=[-1]*len(nums1)
6        for i in range(len(nums2)):
7            while stk and nums2[i]>nums2[stk[-1]]:
8                dic[nums2[stk.pop()]]=nums2[i]
9
10            stk.append(i)
11        for i in range(len(nums1)):
12            if dic[nums1[i]]!=0:
13                res[i]=dic[nums1[i]]
14        return res
15