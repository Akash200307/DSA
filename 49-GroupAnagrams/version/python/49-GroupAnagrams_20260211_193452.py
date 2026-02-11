# Last updated: 2/11/2026, 7:34:52 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        map=defaultdict(list)
4
5        for i in strs:
6            sortedS="".join(sorted(i))
7            map[sortedS].append(i)
8        return list(map.values())
9        