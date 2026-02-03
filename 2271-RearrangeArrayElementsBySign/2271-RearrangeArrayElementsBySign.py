# Last updated: 2/3/2026, 9:36:39 PM
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nArr=[]
        pArr=[]
        res=[]
        vis=set()
        for i in nums:
            if i<0:
                nArr.append(i)
            else:
                pArr.append(i)
        
        for i in range(n//2):
            res.append(pArr[i])
            res.append(nArr[i])
        return res





            
        