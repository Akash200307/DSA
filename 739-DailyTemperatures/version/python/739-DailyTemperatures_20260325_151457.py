# Last updated: 3/25/2026, 3:14:57 PM
1class Solution:
2    def dailyTemperatures(self, temps):
3        results = [0] * len(temps)
4        stack = []
5        for i, temp in enumerate(temps):
6            while stack and temps[stack[-1]] < temp:
7                index = stack.pop()
8                results[index] = i - index
9            stack.append(i)
10
11        return results