# Last updated: 2/3/2026, 9:41:02 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        return " ".join(reversed(words))
