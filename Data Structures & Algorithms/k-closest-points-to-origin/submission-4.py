class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        res = []

        for i, point in enumerate(points):
            minheap.append([((point[0])**2 + (point[1])**2) ** 0.5, i])
        
        heapq.heapify(minheap)

        for i in range(k):
            idx = heapq.heappop(minheap)[1]
            res.append(points[idx])
        return res
