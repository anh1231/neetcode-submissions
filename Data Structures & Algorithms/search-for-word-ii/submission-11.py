class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.idx = -1
        self.refs = 0

    def add_words(self, word, i):
        cur = self
        cur.refs += 1

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.idx = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for i, w in enumerate(words):
            root.add_words(w, i)

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            if (r < 0 or c < 0 or r >= rows or c >= cols
            or board[r][c] == '*' or board[r][c] not in node.children
            or not node.children[board[r][c]]):
                return
            
            tmp = board[r][c]
            prev = node
            node = node.children[tmp]
            board[r][c] = '*'

            if node.idx != -1:
                res.append(words[node.idx])
                node.idx = -1
                node.refs -= 1
                if not node.refs:
                    prev.children[tmp] = None
                    node = None
                    board[r][c] = tmp
                    return
            
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)
            board[r][c] = tmp
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return res