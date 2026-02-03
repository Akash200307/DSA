# Last updated: 2/3/2026, 9:40:18 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset=set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
        