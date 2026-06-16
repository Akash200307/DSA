# Last updated: 6/17/2026, 12:11:43 AM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        mp = defaultdict(int)
4        res = 0
5
6        for num in nums:
7            if not mp[num]:
8                mp[num] = mp[num - 1] + mp[num + 1] + 1
9                mp[num - mp[num - 1]] = mp[num]
10                mp[num + mp[num + 1]] = mp[num]
11                res = max(res, mp[num])
12        return res