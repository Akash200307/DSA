# Last updated: 2/3/2026, 9:44:56 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map={}


        for k,v in enumerate(nums):
            diff=target - v

            if diff in map:
                return [map[diff],k]

            map[v]=k
        return []