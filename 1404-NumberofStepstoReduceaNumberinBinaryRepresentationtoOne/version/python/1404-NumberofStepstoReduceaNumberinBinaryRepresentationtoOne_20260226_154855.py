# Last updated: 2/26/2026, 3:48:55 PM
1class Solution:
2    def numSteps(self, s: str) -> int:
3
4        num=int(s,2)
5
6        steps=0
7        while num!=1:
8            if num%2==0:
9                num//=2
10            else:
11                num+=1
12            steps+=1
13
14
15        return steps