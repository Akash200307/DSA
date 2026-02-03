# Last updated: 2/3/2026, 9:44:29 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort()
        first=strs[0]
        last=strs[-1]
        mini=min(len(first),len(last))
        res=""
        for i in range(mini):
            if first[i]!=last[i]:
                return res
            res+=first[i]
        return res

        