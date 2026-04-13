# Last updated: 4/13/2026, 1:47:33 PM
1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3        if sum(gas)<sum(cost):
4            return -1
5
6        total=res=0
7
8        for i in range(len(gas)):
9            total+=gas[i]-cost[i]
10
11            if total<0:
12                total=0
13                res=i+1
14        return res