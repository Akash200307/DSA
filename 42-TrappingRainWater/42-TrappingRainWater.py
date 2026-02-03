# Last updated: 2/3/2026, 9:43:20 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n
        left_max = 0
        right_max = 0
        res = 0
        for i in range(n):
            j = -i - 1
            left[i] = left_max
            left_max = max(left_max, height[i])
            right[j] = right_max
            right_max = max(right_max, height[j])

        for i in range(n):
            pot = min(left[i], right[i])
            res += max(0, pot - height[i])
        return res
