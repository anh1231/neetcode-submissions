class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotted = set()
        q = deque()
        fresh = 0

        def add_num(r, c):
            nonlocal fresh
            if (min(r,c) < 0 or r == rows or c == cols 
            or (r,c) in rotted or grid[r][c] != 1):
                return
            rotted.add((r,c))
            fresh -= 1
            q.append([r,c])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotted.add((r,c))
                    q.append([r,c])
                elif grid[r][c] == 1:
                    fresh += 1
                

        time = 0

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                add_num(r + 1, c)
                add_num(r - 1, c)
                add_num(r, c + 1)
                add_num(r, c - 1)
            time += 1


        return time if not fresh else -1