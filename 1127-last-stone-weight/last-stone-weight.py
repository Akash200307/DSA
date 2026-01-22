class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums=[-s for s in stones]
        heapq.heapify(nums)

        while len(nums)>1:
            x=heapq.heappop(nums)
            y=heapq.heappop(nums)

            if x!=y:
                heapq.heappush(nums,x-y)
        return -nums[0] if nums else 0