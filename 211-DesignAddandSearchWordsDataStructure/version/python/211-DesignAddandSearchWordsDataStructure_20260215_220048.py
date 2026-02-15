# Last updated: 2/15/2026, 10:00:48 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        
4
5        map=defaultdict(list)
6
7        for i in strs:
8            cur="".join(sorted(i))
9            map[cur].append(i)
10        
11        return list(map.values())
12        
13        
14
15            