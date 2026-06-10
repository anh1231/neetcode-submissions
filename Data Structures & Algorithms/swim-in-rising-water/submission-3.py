class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()

        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        minH = [[grid[0][0], 0, 0]]
        visit.add((0,0))
        while minH:
            t, x, y = heapq.heappop(minH)

            if x == n - 1 and y == n - 1:
                return t
            
            for x1, y1 in directions:
                x2 = x1 + x
                y2 = y1 + y
                if (x2 == n or y2 == n or
                x2 < 0 or y2 < 0 or
                (x2,y2) in visit):
                    continue
                
                visit.add((x2,y2))
                heapq.heappush(minH, [max(grid[x2][y2], t), x2, y2])
        