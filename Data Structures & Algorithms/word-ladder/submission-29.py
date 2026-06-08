class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                new_word = word[:i] + '*' + word[i+1:]
                nei[new_word].append(word)
        
        visit = set()
        q = deque([beginWord])
        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                word = q.popleft()
                visit.add(word)
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for new_word in nei[pattern]:
                        if new_word in visit:
                            continue
                        q.append(new_word)
        
        return 0
                