# Last updated: 2/3/2026, 9:39:13 PM
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:

        # s1=Counter(s)

        # res=sorted(s,key=s1.get,reverse=True)
         
       return "".join( k*v for k,v in Counter(s).most_common())