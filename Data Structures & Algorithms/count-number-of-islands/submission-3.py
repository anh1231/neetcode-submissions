class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            nonlocal res
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '*'):
                return 0
            
            if grid[r][c] == '1':
                grid[r][c] = '*'
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
                return 1
            return 0

        
        for r in range(rows):
            for c in range(cols):
                res += dfs(r,c)
        return res