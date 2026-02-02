class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map={}


        for k,v in enumerate(nums):
            diff=target - v

            if diff in map:
                return [map[diff],k]

            map[v]=k
        return []