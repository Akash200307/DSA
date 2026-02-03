# Last updated: 2/3/2026, 9:42:45 PM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if m==0 and n==1:
            nums1[0]=nums2[0]
            return
        if n==0 and m==1:
            return
        
        temp=[]
        for i in range(m):
            temp.append(nums1[i])
        nums1.clear()
        i,j=0,0
        while i<len(temp) and j<len(nums2):
            if temp[i]<=nums2[j]:
                nums1.append(temp[i])
                i+=1
            else:
                nums1.append(nums2[j])
                j+=1
        
        nums1.extend(temp[i:])
        nums1.extend(nums2[j:])
        