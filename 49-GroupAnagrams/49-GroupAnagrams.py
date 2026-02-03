# Last updated: 2/3/2026, 9:43:16 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map=defaultdict(list)

        for i in strs:
            sortedS="".join(sorted(i))
            map[sortedS].append(i)
        return list(map.values())
        