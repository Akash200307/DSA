# Last updated: 4/6/2026, 5:56:00 PM
1class Solution:
2    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
3        min_heap=[]
4
5        for x,y in points:
6            dis=[x**2 + y**2]
7            min_heap.append((dis,x,y))
8        
9        heapq.heapify(min_heap)
10        res=[]
11        while k>0:
12            dis,x,y=heapq.heappop(min_heap)
13            res.append([x,y])
14            k-=1
15        return res
16
17