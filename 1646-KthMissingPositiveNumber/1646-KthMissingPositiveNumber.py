# Last updated: 2/3/2026, 9:37:21 PM
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low,high=0,len(arr)-1
        while(low<=high):
            mid=low+(high-low)//2

            if arr[mid]-(mid+1)<k:
                low=mid+1
            else:
                high=mid-1
        return k+high+1


        