# Last updated: 3/17/2026, 6:15:20 PM
1class Solution:
2    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
3        maxArea=0
4        m=len(matrix)
5        n=len(matrix[0])
6        hei=[0]*n
7        for i in range(m):
8            for j in range(n):
9                if matrix[i][j]==1:
10                    hei[j]+=1
11                else:
12                    hei[j]=0
13            sh=sorted(hei,reverse=True)
14            for j in range(n):
15                if sh[j]==0:
16                    break
17                maxArea=max(maxArea,sh[j]*(j+1))
18        return maxArea
19