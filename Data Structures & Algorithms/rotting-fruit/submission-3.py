class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotted = set()
        q = deque()
        fruits = 0

        def add_num(r, c):
            if (min(r,c) < 0 or r == rows or c == cols 
            or (r,c) in rotted or grid[r][c] == 0):
                return
            rotted.add((r,c))
            q.append([r,c])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotted.add((r,c))
                    q.append([r,c])
                    fruits += 1
                elif grid[r][c] == 1:
                    fruits += 1
                

        time = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 0
                add_num(r + 1, c)
                add_num(r - 1, c)
                add_num(r, c + 1)
                add_num(r, c - 1)
            if q:
                time += 1

        return time if fruits == len(rotted) else -1