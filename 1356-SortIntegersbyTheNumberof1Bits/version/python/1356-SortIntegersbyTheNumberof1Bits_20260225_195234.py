# Last updated: 2/25/2026, 7:52:34 PM
1class Solution:
2    def sortByBits(self, arr: List[int]) -> List[int]:
3        
4        return sorted(arr,key=lambda x:(x.bit_count(),x))