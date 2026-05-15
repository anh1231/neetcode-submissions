class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = stones
        heapq.heapify_max(max_heap)

        while len(max_heap) > 1:
            l, r = heapq.heappop_max(max_heap), heapq.heappop_max(max_heap)
            new = l - r
            heapq.heappush_max(max_heap, new)
        
        if len(max_heap) == 1:
            return max_heap[0]
        else:
            0