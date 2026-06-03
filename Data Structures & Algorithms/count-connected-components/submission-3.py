class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        comp = 0

        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()

        def bfs(node):
            q = deque([node])
            visit.add(node)

            while q:
                n = q.popleft()
                for i in adj[n]:
                    if i not in visit:
                        q.append(i)
                        visit.add(i)
            
        for i in range(n):
            if i not in visit:
                bfs(i)
                comp += 1
        return comp