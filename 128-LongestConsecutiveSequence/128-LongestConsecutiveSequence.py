# Last updated: 2/3/2026, 9:42:00 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        mx=0
        for num in nums:
            if num-1 not in nums:
                curr=num
                count=0
                while curr in nums:
                    count+=1
                    curr+=1
                mx=max(mx,count)
        return mx

        