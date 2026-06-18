# Last updated: 6/18/2026, 11:59:48 PM
1class Solution:
2    def reverse(self, x: int) -> int:
3        # Handle sign
4        sign = 1 if x >= 0 else -1
5        x = abs(x)
6        
7        reversed_num = 0
8        
9        while x > 0:
10            digit = x % 10
11            # Check for overflow before multiplying/adding
12            if reversed_num > (2**31 - 1) // 10 or \
13               (reversed_num == (2**31 - 1) // 10 and digit > 7):
14                return 0
15            if reversed_num < -(2**31) // 10 or \
16               (reversed_num == -(2**31) // 10 and digit > 8):
17                return 0
18                
19            reversed_num = reversed_num * 10 + digit
20            x //= 10
21            
22        return sign * reversed_num