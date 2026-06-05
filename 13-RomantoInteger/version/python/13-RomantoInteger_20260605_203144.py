# Last updated: 6/5/2026, 8:31:44 PM
1class Solution:
2    def romanToInt(self, s: str) -> int:
3        roman = {
4            'I': 1, 'V': 5, 'X': 10, 'L': 50,
5            'C': 100, 'D': 500, 'M': 1000
6        }
7        
8        total = 0
9        prev = 0
10        
11        # Go from right to left (easiest way to handle subtraction)
12        for ch in reversed(s):
13            curr=roman[ch]
14            if curr<prev:
15                total-=curr
16            else:
17                total+=curr
18            prev=curr
19
20        return total
21