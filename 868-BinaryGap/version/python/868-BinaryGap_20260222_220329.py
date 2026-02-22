# Last updated: 2/22/2026, 10:03:29 PM
1class Solution:
2    def binaryGap(self, n: int) -> int:
3        max_dist = 0
4        curr_dist = 0
5        found_first_one = False
6        
7        while n > 0:
8            bit = n % 2
9            
10            if bit == 1:
11                if found_first_one:
12                    max_dist = max(max_dist, curr_dist)
13                
14                curr_dist = 1
15                found_first_one = True
16            else:
17                if found_first_one:
18                    curr_dist += 1
19            
20            n //= 2
21            
22        return max_dist