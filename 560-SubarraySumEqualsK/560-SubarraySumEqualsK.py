# Last updated: 2/3/2026, 9:38:58 PM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map=defaultdict(int)
        prefix_map[0]=1
        prefix=0
        count=0
        for i in nums:
            prefix+=i
            count+=prefix_map[prefix-k]
            prefix_map[prefix]+=1
        return count
        