# Last updated: 2/15/2026, 9:59:51 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        
4        group_map=collections.defaultdict(list)
5
6        for i in strs:
7
8            s="".join(sorted(i))
9
10            group_map[s].append(i)
11        
12        return list(group_map.values())