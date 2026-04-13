# Last updated: 4/13/2026, 2:45:18 PM
1class Solution:
2    def checkValidString(self, s: str) -> bool:
3        leftMax=leftMin=0
4        for c in s:
5            if c=="(":
6                leftMax+=1
7                leftMin+=1
8            elif c==")":
9                leftMax-=1
10                leftMin-=1
11            else:
12                leftMax+=1
13                leftMin-=1
14            if leftMax<0:
15                return False
16            if leftMin<0:
17                leftMin=0
18        return leftMin==0