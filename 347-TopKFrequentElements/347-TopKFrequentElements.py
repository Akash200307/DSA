# Last updated: 2/3/2026, 9:39:20 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       freq=Counter(nums)
       keyOnly=freq.most_common(k)
       return [i[0] for i in keyOnly]