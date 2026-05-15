class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        heapq.heapify(minheap)
        res = []

        for i, point in enumerate(points):
            heapq.heappush(minheap, [((point[0])**2 + (point[1])**2) ** 0.5, i])

        for i in range(k):
            idx = heapq.heappop(minheap)[1]
            res.append(points[idx])
        return res
