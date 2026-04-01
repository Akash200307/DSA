# Last updated: 4/1/2026, 4:42:53 PM
1class KthLargest:
2
3    def __init__(self, k: int, nums: List[int]):
4        self.k=k
5        self.minheap=nums
6        heapq.heapify(self.minheap)
7        while len(nums)>k:
8            heapq.heappop(self.minheap)
9
10
11    def add(self, val: int) -> int:
12        heapq.heappush(self.minheap,val)
13        if len(self.minheap)>self.k:
14             heapq.heappop(self.minheap)
15        return self.minheap[0]
16        
17        
18
19        
20
21
22# Your KthLargest object will be instantiated and called as such:
23# obj = KthLargest(k, minheap)
24# param_1 = obj.add(val)