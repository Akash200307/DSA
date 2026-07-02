# Last updated: 7/2/2026, 9:38:30 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        length=len(nums)
4        l_arr=[0]*length
5        r_arr=[0]*length
6        l_value=1
7        r_value=1
8        
9        for i in range(length):
10            rev=-i-1
11            l_arr[i]=l_value
12            r_arr[rev]=r_value
13            l_value*=nums[i]
14            r_value*=nums[rev]
15
16        return [i*j for i,j in zip(l_arr,r_arr)]
17
18        