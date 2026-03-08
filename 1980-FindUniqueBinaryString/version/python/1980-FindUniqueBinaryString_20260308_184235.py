# Last updated: 3/8/2026, 6:42:35 PM
1class Solution:
2    def findDifferentBinaryString(self, nums: List[str]) -> str:
3        n=len(nums[0])
4        ans=['0']*n
5        for i, x in enumerate(nums):
6            if x[i]=='0':
7                ans[i]='1'
8            else:
9                ans[i]='0'
10        return "".join(ans)
11                