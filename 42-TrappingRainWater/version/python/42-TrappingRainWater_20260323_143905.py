# Last updated: 3/23/2026, 2:39:05 PM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        n=len(height)
4        l_arr=[0]*n
5        r_arr=[0]*n
6        l_max=r_max=0
7        
8
9        for i in range(n):
10            j= -i-1
11            l_arr[i]=l_max
12            r_arr[j]=r_max
13            l_max=max(l_max,height[i])
14            r_max=max(r_max,height[j])
15        
16        res=0
17
18        for i in range(n):
19            pot=min(l_arr[i],r_arr[i])
20            res+=max(0,pot-height[i])
21        
22        return res