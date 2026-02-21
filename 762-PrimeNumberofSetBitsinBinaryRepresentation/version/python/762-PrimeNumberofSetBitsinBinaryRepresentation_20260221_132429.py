# Last updated: 2/21/2026, 1:24:29 PM
1class Solution:
2    def countPrimeSetBits(self, left: int, right: int) -> int:
3        
4        def is_prime(n):
5            if n < 2:
6                return False
7            if n < 4:
8                return True
9            if n % 2 == 0 or n % 3 == 0:
10                return False
11            i = 5
12            while i <= math.isqrt(n):
13                if n % i == 0 or n % (i + 2) == 0:
14                    return False
15                i += 6
16            return True
17
18
19        count=0
20        for i in range(left,right+1):
21            if is_prime(i.bit_count()):
22                count+=1
23        return count
24       