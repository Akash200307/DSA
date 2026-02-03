# Last updated: 2/3/2026, 9:39:48 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        l_arr=[0]*length
        r_arr=[0]*length
        l_value=1
        r_value=1
        
        for i in range(length):
            rev=-i-1
            l_arr[i]=l_value
            r_arr[rev]=r_value
            l_value*=nums[i]
            r_value*=nums[rev]

        return [i*j for i,j in zip(l_arr,r_arr)]

        