# Last updated: 2/3/2026, 9:36:01 PM
class Solution:
    def reversePrefix(self, s: str, k: int) -> str:

        def reverse(arr):
            return arr[::-1]

        return reverse(s[:k])+s[k:] if k!=len(s)  else reverse(s[:k+1])

       
        