# Last updated: 2/3/2026, 9:40:13 PM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    
        return heapq.nlargest(k,nums)[-1]
            
            