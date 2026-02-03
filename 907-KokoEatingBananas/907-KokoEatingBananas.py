# Last updated: 2/3/2026, 9:38:14 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high=1,max(piles)
        ans=0
        while low<=high:
            mid=low+(high-low)//2
            totalH=0
            for pile in piles:
                totalH+=math.ceil(pile/mid)
            if totalH<=h:
                ans=mid
                high =mid-1
            else:
                low=mid+1
        return ans


                



        