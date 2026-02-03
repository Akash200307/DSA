# Last updated: 2/3/2026, 9:38:28 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start,end=0,len(nums)-1

        while(start<=end):
            mid=end+(start-end)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                start=mid+1
            else:
                end=mid-1
        return -1
        