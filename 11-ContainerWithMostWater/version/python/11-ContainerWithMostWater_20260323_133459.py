# Last updated: 3/23/2026, 1:34:59 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        l,r=0,len(height)-1
4        res=float('-inf')
5        while l<r:
6            length=r-l
7            width=min(height[l],height[r])
8            area=length*width
9
10            res=max(area,res)
11            if height[l]<height[r]:
12                l+=1
13            else:
14                r-=1
15        return res