# Last updated: 2/3/2026, 9:40:55 PM
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid
        return high