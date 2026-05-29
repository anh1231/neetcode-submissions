class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visits = set()
        q = deque()

        def add_num(r, c):
            if (min(r,c) < 0 or r == rows or c == cols
            or (r,c) in visits or grid[r][c] == -1):
                return
            
            visits.add((r,c))
            q.append([r,c])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visits.add((r,c))
                    q.append([r,c])

        dist = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                add_num(r + 1, c)
                add_num(r - 1, c)
                add_num(r, c + 1)
                add_num(r, c - 1)
            dist +=1
