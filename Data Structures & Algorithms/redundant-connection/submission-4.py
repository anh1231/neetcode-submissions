class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        adj = [[] for i in range(n+1)]
        indegree = [0] * (n+1)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        q = deque()
        
        for i in range(n + 1):
            if indegree[i] == 1:
                q.append(i)

        while q:
            node = q.popleft()
            indegree[node] -= 1

            for i in adj[node]:
                indegree[i] -= 1

                if indegree[i] == 1:
                    q.append(i)
        
        for u,v in reversed(edges):
            if indegree[u] > 1 and indegree[v]:
                return [u,v]
        return []