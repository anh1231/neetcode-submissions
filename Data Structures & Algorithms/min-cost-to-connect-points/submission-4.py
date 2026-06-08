class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        seen = set()
        min_heap = [(0, 0)]
        while len(seen) < n:
            cost, node = heapq.heappop(min_heap)
            if node in seen:
                continue

            res += cost
            seen.add(node)
            x1, y1 = points[node]
            for nei, (x2, y2) in enumerate(points):
                if nei not in seen and node != nei:
                    nei_cost = abs(x1-x2) + abs(y1-y2)
                    heapq.heappush(min_heap, (nei_cost, nei))

        return res