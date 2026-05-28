class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c] != 1):
                return 0
            tmp = grid[r][c]
            grid[r][c] = '*'

            total = dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

            return tmp + total
        
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r,c))
        return res