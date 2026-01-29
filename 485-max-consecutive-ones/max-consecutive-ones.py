class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count=0
        count=0

        for i in nums:
            if i==1:
                count+=1
            if i!=1:
                count=0
            max_count=max(count,max_count)
        return max_count