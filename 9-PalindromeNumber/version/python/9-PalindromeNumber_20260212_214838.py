# Last updated: 2/12/2026, 9:48:38 PM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        
4        if x<0:
5            return False
6        con=str(x)
7
8        return con[::-1]==con
9