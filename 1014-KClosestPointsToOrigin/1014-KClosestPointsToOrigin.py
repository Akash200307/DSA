# Last updated: 2/3/2026, 9:37:59 PM
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap=[]

        for x,y in points:
            dis=[x**2+y**2]
            min_heap.append([dis,x,y])
        
        heapq.heapify(min_heap)
        res=[]

        while k>0:
            i,x,y=heapq.heappop(min_heap)
            res.append([x,y])
            k-=1
        return res
            