class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.idx = -1
        self.refs = 0
    
    def add_word(self, word, i):
        cur = self
        cur.refs += 1

        for c in word:
            index = ord(c) - ord('a')
            if not cur.children[index]:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
            cur.refs += 1
        cur.idx = i



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i, w in enumerate(words):
            root.add_word(w, i)

        rows, cols = len(board), len(board[0])
        res = []

        def getIndex(c):
            idx = ord(c) - ord('a')
            return idx
        
        def dfs(r, c, node):
            if (r < 0 or c < 0 or r >= rows or c >= cols 
            or board[r][c] == '*' or not node.children[getIndex(board[r][c])]):
                return
            
            tmp = board[r][c]
            board[r][c] = '*'
            prev = node
            node = node.children[getIndex(tmp)]
            if node.idx != -1:
                res.append(words[node.idx])
                node.idx = -1
                node.refs -= 1
                if not node.refs:
                    prev.children[getIndex(tmp)] = None
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