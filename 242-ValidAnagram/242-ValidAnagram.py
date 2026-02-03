# Last updated: 2/3/2026, 9:39:42 PM
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return Counter(s)==Counter(t)
        