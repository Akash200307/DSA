# Last updated: 2/3/2026, 9:43:33 PM
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def lowerbound():
            ans=-1
            low,high=0,len(nums)-1
            while(low<=high):
                mid=low+(high-low)//2
                if nums[mid]>=target:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans
        def upperbound():
            ans=-1
            low,high=0,len(nums)-1
            while(low<=high):
                mid=low+(high-low)//2
                if nums[mid]>target:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans
            
        lower =lowerbound()
        upper=upperbound()
        if lower == -1 or lower >= len(nums) or nums[lower] != target:
            return [-1,-1]
        if upper == -1:
            return [lower, len(nums) - 1]
        return [lower,upper-1]

        