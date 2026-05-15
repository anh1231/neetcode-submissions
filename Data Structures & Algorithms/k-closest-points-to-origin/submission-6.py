class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        res = []
        heapq.heapify(maxheap)

        for i, point in enumerate(points):
            dist = -(((point[0])**2 + (point[1])**2)**0.5)
            heapq.heappush(maxheap,[dist, i])
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        
        while maxheap:
            point = points[heapq.heappop(maxheap)[1]]
            res.append(point)
        return res
        
        