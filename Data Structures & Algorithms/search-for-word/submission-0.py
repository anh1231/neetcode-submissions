class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        row_len, col_len = len(board), len(board[0])
        visits = set()


        def dfs(i, r, c):
            if i >= len(word):
                return True

            if r < 0 or r >= row_len or c < 0 or c >= col_len:
                return False
            
            if (r, c) in visits:
                return False

            if board[r][c] != word[i]:
                return False

            visits.add((r,c))
            found = (dfs(i + 1, r + 1, c) or \
            dfs(i + 1, r - 1, c) or \
            dfs(i + 1, r, c + 1) or \
            dfs(i + 1, r, c - 1)) 
            visits.remove((r,c))

            return found

        for r in range(row_len):
            for c in range(col_len):
                if dfs(0, r, c):
                    return True
        return False

