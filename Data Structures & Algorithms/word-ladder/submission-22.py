class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        visit = set()

        graph = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                new_word = list(word)
                new_word[i] = '*'
                new_word = "".join(new_word)
                graph[new_word].append(word)
        
        q = deque([beginWord])
        res = 1

        while q:
            res += 1
            for i in range(len(q)):
                word = q.popleft()
                visit.add(word)
                for i in range(len(word)):
                    new_word = list(word)
                    new_word[i] = '*'
                    new_word = "".join(new_word)
                    if new_word in graph:
                        for c in graph[new_word]:
                            if c not in visit:
                                q.append(c)
                            if c == endWord:
                                return res
        return 0
