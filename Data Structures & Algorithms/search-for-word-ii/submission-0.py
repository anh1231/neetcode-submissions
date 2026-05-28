class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isword = False
    
    def add_word(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isword = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.add_word(w)

        rows, cols = len(board), len(board[0])
        res, visits = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= rows or c >= cols 
            or board[r][c] not in node.children
            or (r,c) in visits):
                return
            
            node = node.children[board[r][c]]
            visits.add((r,c))
            word += board[r][c]

            if node.isword:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visits.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, '')
        return list(res)